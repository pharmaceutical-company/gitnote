import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')

class Config:
    def __init__(self, section_name):
    	self.section_name = section_name
    	if not config.has_section(section_name):
    		config.add_section(section_name)
    		self.save()

    def save(self):
    	with open('config.ini', 'wb') as configfile:
    		config.write(configfile)

    def all(self):
    	return config.items(self.section_name)

    def get(self, key, default=None):
        try:
            result = config.get(self.section_name, key)
        except:
            result = default
    	return result or default 

    def set(self, key, value):
    	config.set(self.section_name, key, value)
    	self.save()

    def default(self, key, default=None, prompt=None):
        try:
            value = config.get(self.section_name, key)
        except:
            value = default
            if prompt:
                if isinstance(prompt, str):
                    pass
                elif isinstance(prompt, bool):
                    prompt = '%s.%s' % (self.section_name, key)
                    prompt += (default and ' [%s]? ' % default or '? ')
                    #prompt += prompt.endswith('?') and ' ' or ': '
                rv = raw_input(prompt)
                if rv:
                    value = rv
            if value is not None:
                self.set(key, value)
        return value

    def __getitem__(self, key):
    	return self.get(key)

    def __setitem__(self, key, value):
    	self.set(key, value)


database_config = Config('Database')
database_config.default('url', 'sqlite:///:memory', True)
