# arduino-twitter

A barebones one endpoint API for retrieving a user's latest tweet in JSON format so that it can be queried by an Arduino webserver.

<p>
The arduino webserver cannot handle the size and datatypes returned by the twitter API, this middleware addresses that problem
<p/>

<h5>
Returns a dict containing the timestamp and body of the Tweet
<h5/>
