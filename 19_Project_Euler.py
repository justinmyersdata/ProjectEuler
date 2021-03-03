
def countingsundays():
     '''Returns the number of sundays that fall on the 1st of each month from
     1901 to 2000'''
     days = [31,28,31,30,31,30,31,31,30,31,30,31]

     start = 2
     sundays = 0
     for i in range(1901,2001,1):
          if i%4==0 and i%100!=0:
               days[1] = 29
          else:
               days[1] = 28
          counter = 0
          for day in days:
               counter+=1
               if counter == 12 and i == 2000:
                    break
               #print(i,day,(day+start)%7)
               if (day+start)%7==0:
                    sundays+=1
               start = (day+start)%7

     return(sundays)



countingsundays()