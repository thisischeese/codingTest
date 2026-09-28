def solution(m, musicinfos):
    answer = ""
    answer_length = 0
    
    def get_time(start,end):
        return 60*(int(end[:2])-int(start[:2]))+int(end[3:])-int(start[3:])
        
    def split_music(music):
        target = []
        i=0
        while(i<len(music)):
            if(i<len(music)-1 and music[i:i+2] in ["C#","D#","G#","F#","A#"]):
                    target.append(music[i:i+2])
                    i+=1
            else:
                target.append(music[i])
            i+=1
        return target 
    
    m = split_music(m)
    
    for i in range(len(musicinfos)):
        start,end,music_name,melody=map(str,musicinfos[i].split(","))
        melody = split_music(melody)
        time = get_time(start,end)
        
        temp = (melody*(time//len(melody)+1))[:time]
        for i in range(0,len(temp)-len(m)+1):
            if m==temp[i:i+len(m)] and answer_length<time:
                answer_length=time
                answer = music_name
    
    return "(None)" if answer=="" else answer 

"""

단순히 in으로 대조하면 안된다
"""