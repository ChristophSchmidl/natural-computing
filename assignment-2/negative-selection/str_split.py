import sys, os
import glob
import textwrap

def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

def main(sp_sz, path_train):
	print('working')
	
	#
	# ACT ON TRAINING FILE
	#
	
	# PEN TRAINING FILE AND REMAKE IT
	loc = os.path.dirname(path_train)
	new_loc = loc + '/' + str(sp_sz)
	# CREATE DIRECTORY FOR FILES OF SIZE ...
	if not os.path.exists(new_loc):
		os.makedirs(new_loc)
		
	readfile = open(path_train, 'r')
	linelist = []
	# CREATE LIST OF TEXT IN FILE
	for line in readfile:
		line = line.strip() 
		linelist.append(line)
	readfile.close()
		
	# SPLIT LIST AND CREATE NEW TRAINING FILE IN MAP SPECIFIED BY SIZE	
	new_file = open(new_loc + '/sys_train.train', 'w')
	for line in linelist:
		split_line = split_str(line, sp_sz, skip_tail=False)
		# REMOVE LAST PART IF IT DOESNT FIT IN THE SPECIFIED SIZE
		if (len(split_line[-1]) == sp_sz):
			for item in split_line:
				new_file.write(item + '\n')
		else:
			split_line[-1] = split_line[-1] + "-" * (sp_sz - len(split_line[-1]))
			for item in split_line:
				new_file.write(item + '\n')
	new_file.close()
	
	#
	# ACT ON TEST AND LABEL FILES
	#
	
	# OPENS TESTS FILES IN DIRECTORY, FOR EACH FILE WE CREATE A LIST OF ITS TEXT LINES
	tfile_array = glob.glob(loc + '/*.test')
	
	# ITERATE OVER FILES
	for tfile in tfile_array:
		# OBTAIN THE ASSOCIATED LABEL FILE
		lfile = tfile[:-4] + 'labels'
		
		# CREATE INPUT LIST TO LATER SPLIT UP
		readfile = open(tfile, 'r')
		linelist = []
		# CREATE LIST OF TEXT IN FILE
		for line in readfile:
			line = line.strip() 
			linelist.append(line)
		readfile.close()
		
		# CREATE A LABEL LIST WHICH WILL BE USED TO TAG THE POST SPLIT .TEST FILE
		readfile = open(lfile, 'r')
		lbllist = []
		for line in readfile:
			line = line.strip()
			lbllist.append(line)
		l_len = len(lbllist)
		readfile.close()
		
		# CREATE A NEW TEST AND LABEL FILE 
		new_tfile = open(new_loc + '/' + os.path.basename(tfile), 'w')
		new_lfile = open(new_loc + '/' + os.path.basename(lfile), 'w')
		for i in range(l_len):
			# OBTAIN LABEL
			lbl = lbllist[i]
			
			# SPLIT THE LINE 
			split_line = split_str(linelist[i], sp_sz, skip_tail=False)
			# REMOVE LAST PART IF IT DOESNT FIT IN THE SPECIFIED SIZE
			if (len(split_line[-1]) == sp_sz):
				for item in split_line:
					new_tfile.write(item + '\n')
					new_lfile.write(str(i) + '\n')
			else:
				split_line[-1] = split_line[-1] + "-" * (sp_sz - len(split_line[-1]))
				for item in split_line:
					new_tfile.write(item + '\n')
					new_lfile.write(str(i) + '\n')
		
		new_tfile.close()
		new_lfile.close()
		
	print('Done')
		
if (__name__ == '__main__'):
	if (len(sys.argv) != 3):
		print('Please give us the split size and training file path')
		# EXAMPLE: python str_split.py 5 /home/lumos/University/NC/natural-computing/assignment-2/negative-selection/syscalls/snd-unm/snd-unm.train

	else:
		main(int(sys.argv[1]), sys.argv[2])
