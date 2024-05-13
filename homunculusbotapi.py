
class HomuncBot:
    def __init__(self, txt2sph_f, sph_rec_f, call_when_initialize=None, greet=None):
        for f in call_when_initialize:
            f()
        self.tell = txt2sph_f
        self.sph_rec_f = sph_rec_f
        self._triggers = list()
        self._query = None
        self.free = True
        if isinstance(greet, str):
            txt2sph_f(greet)

    def activate(self, transmission, override=True):
        def wrapper(func):
            def wrapped(*args, **kwargs):
                if (self.query in transmission) or (transmission == 'ANY'):
                    try:
                        func(self.query, *args, **kwargs)
                        self.free = False if override else True
                    except TypeError:
                        func(*args, **kwargs)
                        self.free = False if override else True
            self._triggers.append(wrapped)
            return wrapped
        return wrapper

    @property
    def query(self):
        return self._query

    def poll(self):
        while True:
            self._query = ''
            try:
                self._query = self.sph_rec_f()
            except Exception as e:
                print(f'Error: {e}')
            self.free = True
            for t in self._triggers:
                t()
                if not self.free:
                    break
