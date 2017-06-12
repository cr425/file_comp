import pandas as pd

def files(file1, file2):
    
    content1 = read_file(file1)
    content2 = read_file(file2)
    
    #create dataframe for difference computation
    frame1 = pd.DataFrame(content1, columns = ['content'])
    frame2 = pd.DataFrame(content2, columns = ['content'])
    
    frame1['row'] = frame1.index
    frame2['row'] = frame2.index
    
    frame1 = frame1[['row', 'content']]    
    frame2 = frame2[['row', 'content']]
    
    return frame1, frame2

def read_file(fname):

    with open(fname) as f:
        content = f.readlines()
    	# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    return content

def compute_diff(frame1, frame2):
    
    print '\nDifferences between files:'
    diff_1 = pd.DataFrame()
    diff_2 = pd.DataFrame()
    
    for index, element in enumerate(frame1['content']): 
        if element not in frame2['content'].values:
            diff_1= diff_1.append({'Row:' : str(index), 'Element:': str(element)}, ignore_index=True)     
            
    for index, element in enumerate(frame2['content']): 
        if element not in frame1['content'].values:
            diff_2 = diff_2.append({'Row:' : str(index), 'Element:': str(element)},ignore_index=True)     
          
    if len(diff_1) == 0 and len(diff_2) == 0:
        print 'No Differences'
    else:
        if len(diff_1) <> 0:
            diff_1 = diff_1[['Row:','Element:', ]]
            print '********Changes in File 1********'
            print '\n'
            for row in diff_1.values:
                print diff_1.columns[0] + '\n' + row[0] + '\n' + diff_1.columns[1] + '\n' + row[1] + '\n'
        if len(diff_2) <> 0:
            diff_2 = diff_2[['Row:','Element:', ]]
            print '********Changes in File 2********'
            print '\n'
            for row in diff_2.values:
                print diff_2.columns[0] + '\n' + row[0] + '\n' +  diff_2.columns[1] + '\n' + row[1] + '\n'
       
    print '************End of File Compare************'

    return diff_1, diff_2
   
    
if __name__ == "__main__":
    file1 = raw_input('Please specify file #1 that you want to compare:\n').strip('"')
    file2 = raw_input('Please specify file #2 that you want to compare:\n').strip('"')   
    
    frame1, frame2 = files(file1, file2)

    print '************Starting File Compare************'
    print 'File 1:\n' + str(file1)
    print 'File 2:\n' + str(file2)
    print '*********************************************'

    diff_1, diff_2 = compute_diff(frame1, frame2)