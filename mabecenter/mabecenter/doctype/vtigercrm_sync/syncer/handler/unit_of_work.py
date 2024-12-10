class UnitOfWork:
    def __init__(self, session_factory):
        self.session_factory = session_factory
        
    def __enter__(self):
        self.session = self.session_factory()
        return self.session
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close() 