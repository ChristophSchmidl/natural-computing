import sys, os, glob

def main(score_loc):
	os.chdir(score_loc)
	
	# WE COLLECT ALL SCORE FILES AND MERGE THEM
	for tfile in glob.glob("*.txt"):
		tname = os.path.basename(tfile)
		
		# OBTAIN LINES IN FILE
		readfile = open(tfile, 'r')
		linelist = []
		# CREATE LIST OF TEXT IN FILE
		for line in readfile:
			line = line.strip() 
			linelist.append(line)
		readfile.close()
		
		# CHECK WHICH LABEL FILE WE NEED TO TAKE, THIS IS DONE IN THE MOST UGLY WAY POSSIBLE
		if tname[9] == '1':
			print '1'
			readlbl = open('../snd-cert.1.labels', 'r')
		elif tname[9] == '2':
			print '2'
			readlbl = open('../snd-cert.2.labels', 'r')
		elif tname[9] == '3':
			print '3'
			readlbl = open('../snd-cert.3.labels', 'r')
		elif tname[8] == '1':
			print '1'
			readlbl = open('../snd-unm.1.labels', 'r')
		elif tname[8] == '2':
			print '2'
			readlbl = open('../snd-unm.2.labels', 'r')
		else:
			print '3'
			readlbl = open('../snd-unm.3.labels', 'r')
		
		# READ THE LABELLIST FROM THE LABEL FILE
		lbllist = []
		# CREATE LIST OF TEXT IN FILE
		for lbl in readlbl:
			lbl = lbl.strip() 
			lbllist.append(lbl)
		readlbl.close()
		
		# CREATE NEW FILE TO WHICH WE WRITE THE SCORE
		new_tfile = open(tname[:-4] + '.score', 'w')
		
		# WE ITERATE OVER THE LBL LENGTH AND AVERAGE THE SCORES FOR EACH ACTUAL LABEL
		act_lbl = 0
		n_lbl = 0
		s_lbl = 0
		for i in range(len(lbllist)):
			# IF THE NEXT LABEL IS STILL THE SAME LABEL DO
			if (act_lbl == int(lbllist[i])):
				#ADD SCORE
				n_lbl += 1
				s_lbl += float(linelist[i])
			
			# IF THERE IS A NEW LABEL DO
			else:
				# WRITE THE AVERAGE TO THE FILE
				new_tfile.write(str(s_lbl/float(n_lbl)) + '\n')
				
				# CHANGE ACTUAL LABEL 
				act_lbl += 1
				
				# RESET
				n_lbl = 0
				s_lbl = 0
				
				# ADD SCORE FOR CURRENT LABEL
				n_lbl += 1
				s_lbl += float(linelist[i])
		
if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print('Please give us the score path')
		# EXAMPLE: python score.py /home/lumos/University/NC/natural-computing/assignment-2/negative-selection/syscalls/snd-cert/10/scores
	else:
		main(str(sys.argv[1]))
