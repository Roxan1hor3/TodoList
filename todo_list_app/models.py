import enum

from todo_list_app import db


class MyEnum(enum.Enum):
    archived = 'ARCHIVED'
    open = 'OPEN'


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(MyEnum), default=MyEnum.open, nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    tasks = db.relationship('Task', backref='board', lazy='dynamic')

    def to_dict(self):
        data = {
            'id': self.id,
            'status': self.status.value,
            'created_on': self.created_on.isoformat() + 'Z',
            'updated_on': self.updated_on.isoformat() + 'Z',
            'tasks': [task.to_dict() for task in self.tasks],

        }
        return data


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), nullable=False)
    status = db.Column(db.Boolean, default=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)

    def to_dict(self):
        data = {
            'id': self.id,
            'body': self.body,
            'status': self.status,
            'created_on': self.created_on.isoformat() + 'Z',
            'updated_on': self.updated_on.isoformat() + 'Z',
            'board_id': self.board_id,
        }
        return data

    def from_dict(self, data):
        for field in ['body', 'board_id', 'status']:
            if field in data:
                setattr(self, field, data[field])

    def update_status(self, status):
        setattr(self, 'status', status)
