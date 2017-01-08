function getStatus(queueId) {
    d = new Date();
    now = d.getTime()
    endpoint = "http://localhost:8080/api/v0.1/tournament/status";

    $.ajax({url: endpoint,
	    contentType:"application/json; charset=utf-8",
	    success: function(result){
		        $("#state").text(result.state);
	    },
	    error: function (request, status, error) {
		// Ignore REST API errors, the orchestrartor will bring it back up in time    
	    }
	   });
}
