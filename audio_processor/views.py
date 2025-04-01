from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .transcription import AudioTranscriber
from .summarizer import TextSummarizer
from .title_generator import TitleGenerator
from .models import CallSummary
import os
from pydub import AudioSegment

@api_view(['GET', 'POST'])
def generate_summary(request):
    if request.method == 'GET':
        # Return a simple JSON response for GET requests
        return JsonResponse({'message': 'Please send a POST request with an audio file to generate a summary'})
    
    # Handle POST request
    if 'audio' not in request.FILES:
        return JsonResponse({'error': 'No audio file provided'}, status=400)
    
    audio_file = request.FILES['audio']
    file_path = f"media/temp_{audio_file.name}"
    os.makedirs('media', exist_ok=True)
    
    with open(file_path, 'wb+') as destination:
        for chunk in audio_file.chunks():
            destination.write(chunk)
    
    try:
        audio = AudioSegment.from_file(file_path)
        duration = len(audio) // 1000
        
        call_summary = CallSummary.objects.create(audio_file=audio_file, status='processing')
        
        transcriber = AudioTranscriber()
        transcription_result = transcriber.process_audio(file_path)
        
        if 'error' in transcription_result:
            call_summary.status = 'failed'
            call_summary.save()
            return JsonResponse(transcription_result, status=500)
        
        summarizer = TextSummarizer()
        summary = summarizer.generate_summary(transcription_result['text'])
        
        title_generator = TitleGenerator()
        titles = title_generator.generate_titles(summary)
        
        call_summary.transcription = transcription_result
        call_summary.summary = summary
        call_summary.titles = titles
        call_summary.duration = duration
        call_summary.status = 'completed'
        call_summary.save()
        
        response = {
            'id': call_summary.id,
            'transcription': transcription_result,
            'summary': summary,
            'suggested_titles': titles,
            'duration': duration,
            'created_at': call_summary.created_at.isoformat(),
            'status': call_summary.status
        }
        return JsonResponse(response)
    
    except Exception as e:
        if 'call_summary' in locals():
            call_summary.status = 'failed'
            call_summary.save()
        return JsonResponse({'error': str(e)}, status=500)
    
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
