from  pytube import YouTube

# create a YouTube object (Put your link video)
yt = YouTube("https://www.youtube.com/watch?v=I0n08UXawSg")

# Get the list of available streams
streams = yt.streams.all()

# Select the stream  resolution you want to download 
stream = yt.streams.get_by_resolution("720p")

# To download the video : (Run)
stream.download()

#All Copyrights To Z.Elmansy
