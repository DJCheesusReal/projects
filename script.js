// Function to fetch GitHub pages
function fetchGitHubPages() {
  fetch('https://api.github.com/users/yourusername/repos')
    .then(response => response.json())
    .then(data => {
      const githubPagesDiv = document.getElementById('githubPages');
      const ul = document.createElement('ul');
      data.forEach(repo => {
        if (repo.homepage) {
          const li = document.createElement('li');
          const link = document.createElement('a');
          link.href = repo.homepage;
          link.textContent = repo.name;
          li.appendChild(link);
          ul.appendChild(li);
        }
      });
      githubPagesDiv.appendChild(ul);
    })
    .catch(error => console.error('Error fetching GitHub pages:', error));
}

// Function to fetch YouTube videos
function fetchYouTubeVideos() {
  fetch('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=yourusername&key=yourAPIKey')
    .then(response => response.json())
    .then(data => {
      const uploadsPlaylistId = data.items[0].contentDetails.relatedPlaylists.uploads;
      return fetch(`https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=${uploadsPlaylistId}&maxResults=10&key=yourAPIKey`);
    })
    .then(response => response.json())
    .then(data => {
      const youtubeVideosDiv = document.getElementById('youtubeVideos');
      const ul = document.createElement('ul');
      data.items.forEach(item => {
        const li = document.createElement('li');
        const videoLink = document.createElement('a');
        videoLink.href = `https://www.youtube.com/watch?v=${item.snippet.resourceId.videoId}`;
        videoLink.textContent = item.snippet.title;
        li.appendChild(videoLink);
        ul.appendChild(li);
      });
      youtubeVideosDiv.appendChild(ul);
    })
    .catch(error => console.error('Error fetching YouTube videos:', error));
}

// Call the functions to fetch GitHub pages and YouTube videos when the page loads
window.onload = function() {
  fetchGitHubPages();
  fetchYouTubeVideos();
};
