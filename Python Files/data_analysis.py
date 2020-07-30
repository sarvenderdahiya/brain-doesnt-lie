import matplotlib.pyplot as plt
import csv
from collections import defaultdict
import numpy as np
#from scipy.signal import *
from numpy.fft import * 
#from scipy import *
from pylab import *
#import pywt
import pandas as pd
import statistics

###############----This function averages data points for each second----################## 

def data_processing():
	chan = ['Timestamp','POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta', 'POW.AF4.Alpha', 'POW.AF4.BetaL', 'POW.AF4.BetaH']
	time, af3_theta, af3_alpha, af3_betal, af3_betah, af4_theta, af4_alpha, af4_betal, af4_betah = ([] for i in range(9))
	frequency=0  #counts the frequency
	count=0  #to let me know then the progtam will end. basically counts number of seconds in a video
	
	i=1  #for number of participants
	j=0  #for number of videos
	while i<=6:
		print("i", i)
		j=0
		while j<4:
			print("j",j)
#   ======================================   YOUR PATH GOES HERE   ==================================================
			path_out = "/Your Path/Project/datasets/intermediate_files/video"+str(j)+"_p"+str(i)+".csv"
			fout_data = open(path_out, 'w')

#   ======================================   YOUR PATH GOES HERE   ==================================================
			path_in= "/Your Path/Project/datasets/p"+str(i)+"/p"+str(i)+"_vid_"+str(j)+".csv"
			df = pd.read_csv(path_in, header=1)

			
			df1=df[['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta', 'POW.AF4.Alpha', 'POW.AF4.BetaL', 'POW.AF4.BetaH']]

			for ch in chan:
				if ch=="POW.AF4.BetaH":
					fout_data.write(ch)
				else:
					fout_data.write(ch+",")
			fout_data.write("\n")
			m=0

			while m < (len(df1)):
				frequency=0
	#			print("m", m)
	#			print("\n")
				for n in range(m, len(df1)):

					if int(df1.loc[m, "Timestamp"])== int(df1.loc[n, "Timestamp"]):
						frequency=frequency+1
						
						time.append(df1.loc[n,"Timestamp"])
						af3_theta.append(df1.loc[n, "POW.AF3.Theta"])
						af3_alpha.append(df1.loc[n, "POW.AF3.Alpha"])
						af3_betal.append(df1.loc[n, "POW.AF3.BetaL"])
						af3_betah.append(df1.loc[n, "POW.AF3.BetaH"])
						af4_theta.append(df1.loc[n, "POW.AF4.Theta"])
						af4_alpha.append(df1.loc[n, "POW.AF4.Alpha"])
						af4_betal.append(df1.loc[n, "POW.AF4.BetaL"])
						af4_betah.append(df1.loc[n, "POW.AF4.BetaH"])
					else:
						break
					
				count=count+1
				time_m=statistics.mean(time)
				af3_theta_m=statistics.mean(af3_theta)
				af3_alpha_m=statistics.mean(af3_alpha)
				af3_betal_m=statistics.mean(af3_betal)
				af3_betah_m=statistics.mean(af3_betah)
				af4_theta_m=statistics.mean(af4_theta)
				af4_alpha_m=statistics.mean(af4_alpha)
				af4_betal_m=statistics.mean(af4_betal)
				af4_betah_m=statistics.mean(af4_betah)



				del time[:]
				del af3_theta[:]
				del af3_alpha[:]
				del af3_betal[:]
				del af3_betah[:]
				del af4_theta[:]
				del af4_alpha[:]
				del af4_betal[:]
				del af4_betah[:]

				fout_data.write(str(time_m)+",")
				fout_data.write(str(af3_theta_m)+",")
				fout_data.write(str(af3_alpha_m)+",")
				fout_data.write(str(af3_betal_m)+",")
				fout_data.write(str(af3_betah_m)+",")
			
				fout_data.write(str(af4_theta_m)+",")
				fout_data.write(str(af4_alpha_m)+",")
				fout_data.write(str(af4_betal_m)+",")
				fout_data.write(str(af4_betah_m))
				fout_data.write("\n")
		
				m=m+frequency
				#print(count)
			fout_data.close()
			
			j=j+1
		i=i+1

###############----This function gives graphs for each video and for alpha calibration----##################

def engagement_compositegraph():
	i = 1  # for participants
	j = 0  # for videos
	s = 2
	d = 5
	c1 = 1 + (s / (1 + d))
	c2 = 1 - (s / (1 + d))
	ema_value = []
	ema_time = []
	l_norm=[]
	x_limit = [185, 185, 80, 160]
	df3 = pd.DataFrame(columns=["Time", "p1", "p2", "p3", "p4", "p5", "p6"])

	
	while j < 4:
		print("j", j)
		i = 1
		while i <= 6:
			print("i", i)
#   ======================================   YOUR PATH GOES HERE   ==================================================
			path_in = "/Your Path/Project/datasets/intermediate_files/video" + str(j) + "_p" + str(i) + ".csv"
			df = pd.read_csv(path_in, header=0)
			for k in range(len(df)):
				df.loc[k, "Final_Alpha"] = (df.loc[k, "POW.AF3.Alpha"] + df.loc[k, "POW.AF4.Alpha"]) / 2
				df.loc[k, "Final_Theta"] = (df.loc[k, "POW.AF3.Theta"] + df.loc[k, "POW.AF4.Theta"]) / 2
				df.loc[k, "Final_Beta"] = (((df.loc[k, "POW.AF3.BetaL"] + df.loc[k, "POW.AF3.BetaH"]) / 2) + ((df.loc[k, "POW.AF4.BetaL"] + df.loc[k, "POW.AF4.BetaH"]) / 2)) / 2
				df.loc[k, "Engagement"] = df.loc[k, "Final_Beta"] / (df.loc[k, "Final_Alpha"] + df.loc[k, "Final_Theta"])
				df.loc[k, "Time"] = k
			df2 = pd.DataFrame(columns=["Time", "Engagement"])
			df2["Engagement"] = df["Engagement"]
			df2["Time"] = df["Time"]
			ema_value.append((df2.loc[0, "Engagement"] + df2.loc[1, "Engagement"] + df2.loc[2, "Engagement"] + df2.loc[3, "Engagement"] + df2.loc[4, "Engagement"]) / 5)
			l = 1
			while l < len(df2):
				vi = df2.loc[l, "Engagement"]
				ei = (vi * c1) + ((ema_value[l - 1]) * c2)
				ema_value.append(ei)
				l = l + 1

############========= Normalizing graphs==========#################

			ema_min, ema_max = min(ema_value), max(ema_value)
			for val in ema_value:
				l_norm.append(((val-ema_min) / (ema_max-ema_min))*1)#normalize between 0 and 10
			for m in range(len(l_norm)):
				ema_time.append(m)
			cname = "p"+str(i)
			print("cname", cname)
			df3[cname] = pd.Series(l_norm)
			df3["Time"] = pd.Series(ema_time)

			del ema_value[:]
			del ema_time[:]
			del l_norm[:]

#############======= Without Normalization========#################
			# for m in range(len(ema_value)):
			# 	ema_time.append(m)
			# cname = "p"+str(i)
			# print("cname", cname)
			# df3[cname] = pd.Series(ema_value)
			# df3["Time"] = pd.Series(ema_time)
			#
			# del ema_value[:]
			# del ema_time[:]
###################################################################
			i = i + 1
		
		width=1.5
		plt.figure(dpi=150)
		plt.figure(figsize=(25, 13))
		plt.plot(df3["Time"], df3["p1"], 'b-', linewidth=width, label="Participant 1")
		plt.plot(df3["Time"], df3["p2"], 'k-', linewidth=width, label="Participant 2")
		plt.plot(df3["Time"], df3["p3"], 'm-', linewidth=width, label="Participant 3")
		plt.plot(df3["Time"], df3["p4"], 'c-', linewidth=width, label="Participant 4")
		plt.plot(df3["Time"], df3["p5"], 'g-', linewidth=width,label="Participant 5")
		plt.plot(df3["Time"], df3["p6"], 'r-', linewidth=width,label="Participant 6")
		if j==0:
			plt.title("Alpha calibration for all participants")
			plt.ylabel("Alpha")
		else:
			title="Engagement graph for video"+str(j)
			plt.title(title)
			plt.ylabel('Engagement')
		plt.xlabel('Time(s)')
		plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)# borderaxespad=0.
		plt.xlim(0, x_limit[j])
		#plt.xlim(20,50)
		plt.xticks(np.arange(0, x_limit[j], step = 5))

		plt.grid(True)
#   ======================================   YOUR PATH GOES HERE   ==================================================
		image_path = "/Your Path/Project/graphs/video" + str(j) + ".png"
		plt.savefig(image_path, bbox_inches='tight')
		j = j + 1


def main():
	data_processing()  # Takes average of data points for each second
	print("\n")
	print("\n")
	engagement_compositegraph()  # Gives engagement graphs for each video and also alpha calibration


main()  # Program execution starts from here




