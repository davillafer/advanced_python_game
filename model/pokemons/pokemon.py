class Pokemon:

    def __init__(self, name, types, life, had_state=False, state=None):
        self.name = name
        self.types = types
        self.life = life
        self.had_state = had_state  # Debe ir delante de state
        self.state = state

    def __setattr__(self, key, value):
        if key == 'state':
            if not self.had_state and value is not None:
                super().__setattr__(key, value)
                super().__setattr__('had_state', True)
            else:
                super().__setattr__(key, None)
        elif key == 'life':
            if value < 0:
                super().__setattr__(key, 0)
            else:
                super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    def has_effect(self):
        return self.state is not None

    def apply_effect(self):
        if self.has_effect():
            # self.life =
            self.state.effect(self)
