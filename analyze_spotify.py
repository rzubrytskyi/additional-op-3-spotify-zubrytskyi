import pandas as pd

data_path = 'top_50_2023.csv'
spotify_data = pd.read_csv(data_path)

spotify_data['genres'] = spotify_data['genres'].apply(eval)
spotify_data['album_release_date'] = pd.to_datetime(spotify_data['album_release_date'])

# Average danceability
total_danceability = 0
for danceability in spotify_data['danceability']:
    total_danceability += danceability
average_danceability = total_danceability / len(spotify_data['danceability'])
print("Average Danceability:", average_danceability)

# Release date difference
max_popularity = spotify_data['popularity'].max()
min_popularity = spotify_data['popularity'].min()
most_popular_track_date = spotify_data[spotify_data['popularity'] == max_popularity]['album_release_date'].iloc[0]
least_popular_track_date = spotify_data[spotify_data['popularity'] == min_popularity]['album_release_date'].iloc[0]

date_difference = (most_popular_track_date - least_popular_track_date).days
print("Days between release dates of most and least popular tracks:", date_difference)

# Top three genres
genre_list = []
for genres in spotify_data['genres']:
    genre_list.extend(genres)
genre_count = {}
for genre in genre_list:
    if genre in genre_count:
        genre_count[genre] += 1
    else:
        genre_count[genre] = 1

sorted_genres = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top Three Genres:")
for genre, count in sorted_genres:
    print(genre, count)

# Average liveliness
total_liveliness = 0
count_high_energy_tracks = 0
for index, row in spotify_data.iterrows():
    if row['energy'] > 0.5:
        total_liveliness += row['liveness']
        count_high_energy_tracks += 1
average_liveliness = total_liveliness / count_high_energy_tracks
print("Average Liveliness for high energy tracks:", average_liveliness)

# Recurring artists
artist_count = {}
for artist in spotify_data['artist_name']:
    if artist in artist_count:
        artist_count[artist] += 1
    else:
        artist_count[artist] = 1

recurring_artists = {artist: count for artist, count in artist_count.items() if count > 1}
print("Recurring Artists and their Tracks:")
for artist in recurring_artists.keys():
    tracks = spotify_data[spotify_data['artist_name'] == artist]['track_name'].tolist()
    print(artist, ": ", tracks)