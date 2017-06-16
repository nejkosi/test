def createQuery(us1, startdate=None, enddate=None):
    
    import dateutil.parser, time
    
    def toNum(datestring):
        d = dateutil.parser.parse(datestring)
        return time.mktime(d.timetuple())
    
    my_list = [
                {"$match" : {"user.hash-user-id": us1}},
                {"$match" : {"event.timestamp" : {"$gte" : toNum(startdate),"$lt" : toNum(enddate)}}},
                {"$match" : {"event.content.original-title" : {"$exists" : "True"}}},
                {"$project" : {"ISOtime":"$event.time-to-iso",
                             "tv_show":"$event.content.original-title",
                            "tv_ch":{"$ifNull":["$event.channel.id",'N/A']}}}
                #{"$group" : {"_id":"$user.hash-user-id"}}
              ]
    
    return my_list