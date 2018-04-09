def log_operation(user_id,operation,auth,success ):
	#The user ID is an interger determined by looking up the auth token in the token database and 
	#returning the associated user ID. The ID is passed to the logging function as an interger. The
	#operation is a character value, defined by its corresponding CRUD value. For example, you would
	#pass a value of 'c' for a create operation or a value of 'u' for an update operation. The auth 
	#parameter specifies whether the attemped action was allowed or not. If a user attempted to create
	#a table entry but did not have proper authority, auth would be FALSE. If a user attempted to 
	#read a table entry and was permitted to do so, auth would be TRUE. Lastly, success is for error
	#logging purposes only. If a user attemped to add a table entry and is authorized to do so but 
	#there is a database error, a value of FALSE would be passed for success. If the operation is
	#successful, TRUE is passed.

	import logging

	#TODO operation toLower

	#TODO absolute path of log file destination
	#log_file = example

	#template for log messages
	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filename='example.log', level=logging.DEBUG)

	#perform standard logging operations if requested operation was successful
	if success == True:
		#attempted CREATE operation
		if operation == 'c':
			if auth:
				#CREATE, authorized, no error
				logging.info('user=%d successfuly created an entry in the table', user_id)
			else:
				#CREATE, unauthorized, no error
				logging.warning('user=%d attempted to perform an unauthorized creation operation', user_id)
		#attempted READ operation
		elif operation == 'r':
			if auth:
				#READ, authorized, no error
				logging.info('user=%d successfuly read an entry in the table', user_id)
			else:
				#READ, unauthorized, no error
				logging.warning('user=%d attempted to perform an unauthorized read operation', user_id)
		#attempted UPDATE operation
		elif operation == 'u':
			if auth:
				#UPDATE, authorized, no error
				logging.info('user=%d successfuly updated an entry in the table', user_id)
			else:
				#UPDATE, unauthorized, no error
				logging.warning('user=%d attempted to perform an unauthorized update operation', user_id)
		#attempted DELETE operation
		elif operation == 'd':
			if auth:
				#DELETE, authorized, no error
				logging.info('user=%d successfuly deleted an entry in the table', user_id)
			else:
				#DELETE, unauthorized, no error
				logging.warning('user=%d attempted to perform an unauthorized deletion operation', user_id)
		#improper argument error checking
		else:
			logging.debug('IMPROPER OPERATION VARIABLE PASSED TO FUNCTION')
	#log error message if requested operation was not successful
	else:
		#attempted CREATE operation failed
		if operation == 'c':
			if auth:
				#CREATE, authorized, error
				logging.error('user=%d attmpted to perform an authorized creation operation, but encountered an error', user_id)
			else:
				#CREATE, unauthorized, error
				logging.error('user=%d attmpted to perform an unauthorized creation operation, but encountered an error', user_id)
		#attempted READ operation failed
		elif operation == 'r':
			if auth:
				#READ, authorized, error
				logging.error('user=%d attmpted to perform an authorized read operation, but encountered an error', user_id)
			else:
				#READ, unauthorized, error
				logging.error('user=%d attmpted to perform an unauthorized read operation, but encountered an error', user_id)
		#attempted UPDATE operation failed
		elif operation == 'u':
			if auth:
				#UPDATE, authorized, error
				logging.error('user=%d attmpted to perform an authorized update operation, but encountered an error', user_id)
			else:
				#UPDATE, unauthorized, error
				logging.error('user=%d attmpted to perform an unauthorized update operation, but encountered an error', user_id)
		#attempted DELETE operation failed
		elif operation == 'd':
			if auth:
				#DELETE, authorized, error
				logging.error('user=%d attmpted to perform an authorized delete operation, but encountered an error', user_id)
			else:
				#DELETE, unauthorized, error
				logging.error('user=%d attmpted to perform an unauthorized delete operation, but encountered an error', user_id)
		#improper argument error checking
		else:
			logging.debug('IMPROPER OPERATION VARIABLE PASSED TO FUNCTION')
	return;

#test function calls

#authorized, no error
log_operation(1234,'c',True,True)
log_operation(1234,'r',True,True)
log_operation(1234,'u',True,True)
log_operation(1234,'d',True,True)
log_operation(1234,'z',True,True)

#unauthorized, no error
log_operation(1234,'c',False,True)
log_operation(1234,'r',False,True)
log_operation(1234,'u',False,True)
log_operation(1234,'d',False,True)
log_operation(1234,'z',False,True)

#authorized, with error
log_operation(1234,'c',True,False)
log_operation(1234,'r',True,False)
log_operation(1234,'u',True,False)
log_operation(1234,'d',True,False)
log_operation(1234,'z',True,False)

#unauthorized, with error
log_operation(1234,'c',False,False)
log_operation(1234,'r',False,False)
log_operation(1234,'u',False,False)
log_operation(1234,'d',False,False)
log_operation(1234,'z',False,False)