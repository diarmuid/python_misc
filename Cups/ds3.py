import logging
logging.basicConfig(level=logging.ERROR)


good_sequence =  [         3, 4, 5, 6, 7, 8, 9, 10,11,12,13,0xdead,0xbeef,\
                  14,15,16,17,18,19,20,21,22,23,24,25,26,27,0xdead,0xbeef,\
                  28,29,30]
bad_sequence1 =  [         3, 4, 5, 6, 7, 8, 9, 10,11,12,13,0xdead,0xbeef,\
                  14,15,16,17,18,19,20,22,22,23,24,25,26,27,0xdead,0xbeef,\
                  28,29,30]
bad_sequence2 =   [         3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,0xbeef,\
                  14,15,16,17,18,19,20,21,22,23,24,25,26,27,0xdead,0xbeef,\
                  28,29,30]
                  


def CheckSequence(input_sequence):
    
    previous_val = None # Previous number seen
    count_to_16 = None # Running count of inputs
    error_count = 0 # Count of errors
    
    for value in input_sequence:
        #logging.debug("Value={}".format(value))
        
        # Initialize the counter
        if count_to_16 == None:
            count_to_16 = value % 14
        # Initialize the previous val    
        if previous_val == None:
            previous_val = value
        else:
            if value == 0xdead:
                if (count_to_16+1) % 16 != 14:
                    logging.debug("Error at 0x{:x} {}".format(value,count_to_16))
                    error_count += 1
            elif value == 0xbeef:
                if (count_to_16+1) % 16 != 15:
                    logging.debug("Error at 0x{:x} {}".format(value,count_to_16))
                    error_count += 1
            elif previous_val +1 != value:
                logging.debug("Error at {:x} prev={}".format(value,previous_val))
                previous_val = value
                error_count += 1
            else:
                logging.debug("ok")
                previous_val = value
            count_to_16 += 1
            
    return error_count
            

print CheckSequence(good_sequence)
print CheckSequence(bad_sequence1)
print CheckSequence(bad_sequence2)
