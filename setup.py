import datetime
import links

#If you want the code to work for yourself make a python file called links and add the links you want in there

link = ''

def main(hrs, mins, day):

    #How many mins before class starts do you want it to start joining
    leeway = 2



    def monday():
        global link

        #8:00 - 8:10:
        if hrs == 8 and mins < 10-leeway:
            #FIXME idk the link for it yet this just sets it to an empty str
            link = links.morning

        #8:10 - 9:30
        elif hrs == 8 and mins >= 10-leeway or hrs == 9 and mins < 30-leeway:
            link = links.english
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.ap_history

        #10:45 - 11:45
        elif hrs == 10 and mins >= 45-leeway or hrs == 11 and mins < 45-leeway:
            link = links.ap_history

        #11:45 - 12:45
        elif hrs == 11 and mins >= 45-leeway or hrs == 12 and mins < 45-leeway: 
            link = links.pe

        #12:45 - 1:05       
        elif hrs == 12 and mins >= 45-leeway or hrs == 13 and mins < 5-leeway:
            link = links.assembly

        #1:45 - 3:00           
        elif hrs == 13 and mins >= 45-leeway or hrs == 14 or hrs == 15:
            link = links.precalc
        
        else:
            link = ''

   
    def tuesday():

        global link

        #8:00 - 8:10:
        if hrs == 8 and mins < 10-leeway:
            #FIXME idk the link foret this just sets it to an empty str
            link = links.morning_quran

        #8:10 - 9:30
        elif hrs == 8 and mins >= 10-leeway or hrs == 9 and mins < 30-leeway:
            link = links.ap_history
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.islamic_studies_salim

        #10:45 - 11:45
        elif hrs == 10 and mins >= 45-leeway or hrs == 11 and mins < 45-leeway:
            link = links.quran

        else:
            link = '' 

    def wednesday():

        global link

        #8:00 - 8:10:
        if hrs == 8 and mins < 10-leeway:
            #FIXME idk the link for it yet this just sets it to an empty str
            link = links.morning_quran

        #8:10 - 9:30
        elif hrs == 8 and mins >= 10-leeway or hrs == 9 and mins < 30-leeway:
            link = links.english
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.mafahim

        #10:45 - 11:45
        elif hrs == 10 and mins >= 45-leeway or hrs == 11 and mins < 45-leeway:
            link = links.mafahim

        #11:45 - 12:45
        elif hrs == 11 and mins >= 45-leeway or hrs == 12 and mins < 45-leeway: 
            link = links.ap_history
        

        #12:45 - 1:05
        elif hrs == 12 and mins >= 45-leeway or hrs == 13 and mins < 5-leeway:
            link = links.assembly

        #1:45 - 3:00
        elif hrs == 13 and mins >= 45-leeway or hrs == 14 or hrs == 15:
            pass
            #NOTE theres three different islamic studies on wednesday and it rotates so just ignore it for now
            # link = links.islamic_studies_salim

        else:
            link = '' 


    def thursday():

        global link

        #8:00 - 8:10:
        if hrs == 8 and mins < 10-leeway:
            #FIXME idk the link for morning quran yet so this just sets it to an empty str
            link = links.morning_quran

        #8:10 - 9:30
        elif hrs == 8 and mins >= 10-leeway or hrs == 9 and mins < 30-leeway:
            link = links.ap_history
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.us_govt

        #10:45 - 11:45
        elif hrs == 10 and mins >= 45-leeway or hrs == 11 and mins < 45-leeway:
            link = links.us_govt

        else:
            link = '' 

    def friday():

        global link

        #8:00 - 8:10
        if hrs == 8 and mins < 10-leeway:
            #FIXME idk the link for it yet this just sets it to an empty str
            link = links.morning_quran

        #8:10 - 9:30
        elif hrs == 8 and mins >= 10-leeway or hrs == 9 and mins < 30-leeway :
            link = links.english
        
        else:
            link = '' 

    def weekday():
        #here based on which weekday it is it executes the corresponding function

        if day == 1:
            monday()
        
        elif day == 2:
            tuesday()

        elif day == 3:
            wednesday()

        elif day == 4:
            thursday()
        
        elif day == 5:
            friday()

    weekday()