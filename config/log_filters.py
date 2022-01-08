from logging import Filter
from pprint import pprint


class ManagementFilter(Filter):

	def filter(self, record):
		if ishasattr(record, 'funcName') and record.funcName == 'execute':
			return False
		return True


# Noe: Not yet implemented
