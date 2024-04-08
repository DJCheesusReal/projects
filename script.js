// scripts.js
$(document).ready(function() {
  // Fetch recent videos using YouTube API
  $.get("https://www.googleapis.com/youtube/v3/playlistItems", {
      part: "snippet",
      maxResults: 6,
      playlistId: "PLAtYOkqenIuyhjn4b95fAEQww_wlrJtJx",
      key: "AIzaSyDdawYUcr7uqJbhG376CHnG34ULpivpECY"
  }, function(data) {
      if (data.items) {
          var videosHtml = '';
          $.each(data.items, function(index, item) {
              var videoId = item.snippet.resourceId.videoId;
              var videoTitle = item.snippet.title;
              var videoThumbnail = item.snippet.thumbnails.medium.url;
              var videoLink = "https://www.youtube.com/watch?v=" + videoId;
              videosHtml += '<div class="video"><a href="' + videoLink + '"><img src="' + videoThumbnail + '" alt="' + videoTitle + '"><h3>' + videoTitle + '</h3></a></div>';
          });
          $('.videos').html(videosHtml);
      }
  });

  // Embed Twitter timeline
  twttr.widgets.createTimeline(
      {
          sourceType: "profile",
          screenName: "dj_cheesusyt"
      },
      document.getElementById("twitter-feed")
  );
});
