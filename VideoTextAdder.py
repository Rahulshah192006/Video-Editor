from moviepy.editor import *
print("This is an simple Video editor made in python to add text")


location = input("Enter The location of video:")
text = input("Enter the text to add on Video:")
fontsize = input("Enter font size:")
color = input("Enter the color of text:")
Position = input("Enter The position of text ex bottom left right etc:")
duration = input("Enter Duration Of video:")
FPS = input("Enter The FPS:")
videofilename = input("Enter The name of output file:")
video = VideoFileClip(f"{location}").subclip(50,60)
txt_clip = ( TextClip(f"{text}",fontsize=fontsize,color=f'{color}')
            .set_position(f'{Position}')
            .set_duration(duration) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile(f"{videofilename}",fps=300)
    