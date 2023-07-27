from django.shortcuts import render


def tutorial(request):
    video_path = 'videos/test_video.webm'  # Update the video file path
    context = {
        'heading': 'Welcome to the New Page',
        'text': 'This is some basic text for the new page.',
        'video_path': video_path,
    }
    return render(request, 'tutorial.html', context)

