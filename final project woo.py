# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:39:51 2018

@author: Nadia
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas
locations = {"GA": "Georgia", "NY" : "New York", "NC" : "North Carolina", "PA" : "Pennsylvania", "RI": "Rhode Island", "SC" : "South Carolina", "US" : "United States", "all" : "six states, one country, and two diseases"}
diseases = {"salm" : "Salmonellosis", "stec" : "STEC"}
years = np.array([2012, 2013, 2014, 2015, 2016])

def GAsalm():
    G_salmx = years
    G_salmy = np.array([28.3, 26.7, 26.9, 23, 22.4])
    plt.plot(G_salmx,G_salmy)
    plt.title("Incidence of Salmonellosis per 100,000 in Georgia 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (G_salmx, G_salmy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def GAstec():
    G_stecx = years
    G_stecy = np.array([1.9, 1.43, 0.93, 1.0, 1.15])
    plt.plot(G_stecx,G_stecy)
    plt.title("Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 in Georgia 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (G_stecx, G_stecy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def NYsalm():
    NY_salmx = years
    NY_salmy = np.array([14.1,13.1, 13.1, 12.4, 11.8])
    plt.plot(NY_salmx,NY_salmy)
    plt.title("Incidence of Salmonellosis per 100,000 in New York 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (NY_salmx, NY_salmy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def NYstec():
    NY_stecx = years
    NY_stecy = np.array([1.6, 1.5, 1.4, 1.9, 1.9])
    plt.plot(NY_stecx,NY_stecy)
    plt.title("Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 in New York 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (NY_stecx, NY_stecy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def NCsalm():
    NC_salmx = years
    NC_salmy = np.array([25, 26.6, 22.8, 28, 24.1])
    plt.plot(NC_salmx,NC_salmy)
    plt.title("Incidence of Salmonellosis per 100,000 in North Carolina 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (NC_salmx, NC_salmy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def NCstec():
    NC_stecx = years
    NC_stecy = np.array([2.26, 1.18, 1.07, 1.62, 3.32])
    plt.plot(NC_stecx,NC_stecy)
    plt.title("Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 in North Carolina 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (NC_stecx, NC_stecy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def PAsalm():
    P_salmx = years
    P_salmy = np.array([15, 14.8, 13.8, 12.7, 11.5])
    plt.plot(P_salmx,P_salmy)
    plt.title("Incidence of Salmonellosis per 100,000 in Pennsylvania 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (P_salmx, P_salmy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def PAstec():
    P_stecx = years
    P_stecy = np.array([1.38, 1.94, 1.73, 2.0, 1.92])
    plt.plot(P_stecx,P_stecy)
    plt.title("Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 in Pennsylvania 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (P_stecx, P_stecy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def RIsalm():
    R_salmx = years
    R_salmy = np.array([16.6, 18.4, 10.3, 12.2, 13.3])
    plt.plot(R_salmx,R_salmy)
    plt.title("Incidence of Salmonellosis per 100,000 in Rhode Island 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (R_salmx, R_salmy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def RIstec():
    R_stecx = years
    R_stecy = np.array([3.3, 2.0, 0.85, 1.61, 1.04])
    plt.plot(R_stecx,R_stecy)
    plt.title("Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 in Rhode Island 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (R_stecx, R_stecy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def SCsalm():
    S_salmx = years
    S_salmy = np.array([37.6, 34.1, 31.1, 24.1, 29.3])
    plt.plot(S_salmx,S_salmy)
    plt.title("Incidence of Salmonellosis per 100,000 in South Carolina 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (S_salmx, S_salmy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def SCstec():
    S_stecx = years
    S_stecy = np.array([1.3, 0.59, 0.43, 1.18, 0.79])
    plt.plot(S_stecx,S_stecy)
    plt.title("Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 in South Carolina 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (S_stecx, S_stecy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def USsalm():
    U_salmx = years
    U_salmy = np.array([17.7, 16.8, 17.3, 16.1, 16.3])
    plt.plot(U_salmx,U_salmy)
    plt.title("Incidence of Salmonellosis per 100,000 in the United States 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (U_salmx, U_salmy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def USstec():
    U_stecx = years
    U_stecy = np.array([2.1, 1.55, 1.39, 1.78, 2.53])
    plt.plot(U_stecx,U_stecy)
    plt.title("Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 in the United States 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.table(cellText = (U_stecx, U_stecy), loc = 'bottom', bbox=[0.25, -0.5, 0.5, 0.3])
    plt.show()
    
def combinedsalm():
    c_salmx = years
    c_salmy1 = np.array([28.3, 26.7, 26.9, 23, 22.4])
    plt.plot(c_salmx,c_salmy1)
    c_salmy2 = np.array([14.1,13.1, 13.1, 12.4, 11.8])
    plt.plot(c_salmx,c_salmy2)
    c_salmy3 = np.array([25, 26.6, 22.8, 28, 24.1])
    plt.plot(c_salmx,c_salmy3)
    c_salmy4 = np.array([15, 14.8, 13.8, 12.7, 11.5])
    plt.plot(c_salmx,c_salmy4)
    c_salmy5 = np.array([16.6, 18.4, 10.3, 12.2, 13.3])
    plt.plot(c_salmx,c_salmy5)
    c_salmy6 = np.array([37.6, 34.1, 31.1, 24.1, 29.3])
    plt.plot(c_salmx,c_salmy6)
    c_salmy7 = np.array([17.7, 16.8, 17.3, 16.1, 16.3])
    plt.plot(c_salmx, c_salmy7)
    plt.title("Combined Incidence of Salmonellosis per 100,000 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.legend(("GA", "NY", "NC", "PA", "RI", "SC", "US"))
    plt.show()
    
def combinedstec():
    c_stecx = years
    c_stecy1 = np.array([1.9, 1.43, 0.93, 1.0, 1.15])
    plt.plot(c_stecx,c_stecy1)
    c_stecy2 = np.array([1.6, 1.5, 1.4, 1.9, 1.9])
    plt.plot(c_stecx,c_stecy2)
    c_stecy3 = np.array([2.26, 1.18, 1.07, 1.62, 3.32])
    plt.plot(c_stecx,c_stecy3)
    c_stecy4 = np.array([1.38, 1.94, 1.73, 2.0, 1.92])
    plt.plot(c_stecx,c_stecy4)
    c_stecy5 = np.array([3.3, 2.0, 0.85, 1.61, 1.04])
    plt.plot(c_stecx,c_stecy5)
    c_stecy6 = np.array([1.3, 0.59, 0.43, 1.18, 0.79])
    plt.plot(c_stecx,c_stecy6)
    c_stecy7 = np.array([2.1, 1.55, 1.39, 1.78, 2.53])
    plt.plot(c_stecx, c_stecy7)
    plt.title("Combined Incidence of Shiga-toxin Producing E. Coli (STEC) per 100,000 2012-2016")
    plt.xticks(np.arange(2012, 2017, 1))
    plt.legend(("GA", "NY", "NC", "PA", "RI", "SC", "US"))
    plt.show()

def welcome():
    print("Welcome to the Communicable Disease Tracker. Please enter the two-letter postal code of a state or country. To view statistics for all locations, type 'all'.")
    state = input("Enter a location: ")
    if len(state) > 3 or len(state) < 2:
        print("Please make sure your input is no less than two characters and no more than three.")
        while True:
                restart = input("Restart? Yes or no? ")
                if restart == "Yes" or restart == "yes":
                    welcome()
                    break
                elif restart == "No" or restart == "no":
                    print("Goodbye!")
                    break
                else: 
                    print("Try again!")
    else:
        if state in locations:
            print ("There is data available for " + locations[state] + ".")
            def tracker():
                ill = input("Please enter a disease (salm, stec): ")
                if ill in diseases:
                    if state in locations:
                        response = input("Would you like a graph of the data? ")
                        if response == "no":
                            pass
                        elif response == "yes":
                            if ill == "salm" and state == "GA":
                                return GAsalm()
                            elif ill == "stec" and state == "GA":
                                return GAstec()
                            elif ill == "salm" and state == "NY":
                                return NYsalm()
                            elif ill == "stec" and state == "NY":
                                return NYstec()
                            elif ill == "salm" and state == "NC":
                                return NCsalm()
                            elif ill == "stec" and state == "NC":
                                return NCstec()
                            elif ill == "salm" and state == "PA":
                                return PAsalm()
                            elif ill == "stec" and state == "PA":
                                return PAstec()
                            elif ill == "salm" and state == "RI":
                                return RIsalm()
                            elif ill == "stec" and state == "RI":
                                return RIstec()
                            elif ill == "salm" and state == "SC":
                                return SCsalm()
                            elif ill == "stec" and state == "SC":
                                return SCstec()
                            elif ill == "salm" and state == "US":
                                return USsalm()
                            elif ill == "stec" and state == "US":
                                return USstec()
                            elif ill == "salm" and state == "all":
                                return combinedsalm()
                            elif ill == "stec" and state == "all":
                                return combinedstec()
                            else:
                                print ("Unavailable")
                        else:
                            tryagain = input("Try again. ")
                            if tryagain == "yes" or "no":
                                print(response)
                else:
                    print("Pathogen was not found.")
            tracker()
            ask1 = input("Would you like to see all data? ")
            if ask1 == "yes" or ask1 == "Yes":
                with open('communicablediseasechart.csv') as CDC:
                    reader = pandas.read_csv(CDC)
                    print(reader)
                CDC.close()
                print("Data sourced from the Centers for Disease Control and Prevention (CDC) and state health departments.")
            else:
                print("Data sourced from the Centers for Disease Control and Prevention (CDC) and state health departments.")
                ask2 = input("Would you like to see more graphs? ")
                if ask2 == "yes" or ask2 == "Yes":
                    welcome()
                else:
                    print("Goodbye!")
        else:
            print("We're sorry, there is no data available. Please try again or enter a different state.")
            while True:
                restart = input("Restart? Yes or no? ")
                if restart == "Yes" or restart == "yes":
                    welcome()
                    break
                elif restart == "No" or restart == "no":
                    print("Goodbye!")
                    break
                else: 
                    print("Try again!")

welcome()
    