select * from feed limit 1;
 id |  titles| url       |   author   | category |    date    |   imageurl |  description                 
 --------+--------                                                       
 17 | The Intelligent Storage Revolution | https://dzone.com/articles/the-intelligent-storage-revolution | ctsmithiii | cloud    | 2022-02-18 | https://dz2cdn3.dzone.com/storage/article-thumb/15592030-thumb.jpg | Kalista is leading the intelligent storage revolution with computing and storage systems designed for software environments and next-gen storage devices.

select * from tags limit 1;
 id | tag        | description                                                  
  1 | javascript | For questions regarding programming in ECMAScript (JavaScript/JS) and its various dialects/implementations (excluding ActionScript). Note JavaScript is NOT the same as Java! Please include all relevant tags on your question; e.g., [node.js], [jquery], [json], [reactjs], [angular], [ember.js], [vue.js], [typescript], [svelte], etc.

select * from connect;
 postid | tagsid 
   620  |   1254

select feed.titles, tags.tag, feed.url from feed inner join connect on feed.id = connect.postid inner join tags on connect.tagsid = tags.id;

