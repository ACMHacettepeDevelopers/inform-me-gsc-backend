from podcast import PodcastGenerator

pd = PodcastGenerator()

country_code = "US"
q = "economy"
count = 5
file_name = "debug.mp3"
debug_mode = True

pd.create_podcast(country_code=country_code,q=q,count = count,podcast_file_name= file_name,debug_mode=debug_mode)
pd.create_podcast(country_code=country_code,q=q,count = count,podcast_file_name="prod.mp3",debug_mode=False)