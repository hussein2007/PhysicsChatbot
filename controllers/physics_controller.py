class PhysicsController:
    def __init__(self, physics_model):
        self.physics_model = physics_model

    def respond(self, user_input):
        return self.physics_model.get_response(user_input)