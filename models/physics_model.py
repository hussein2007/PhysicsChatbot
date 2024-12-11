class PhysicsModel:
    def __init__(self):
        self.knowledge_base = {
            "نيوتن": "قانون نيوتن الأول: لا يتحرك الجسم إلا إذا أثرت عليه قوة.",
            "الطاقة": "الطاقة هي القدرة على أداء عمل.",
            "القوة": "القوة هي التأثير الذي يغير حركة الجسم.",
            "الحركة": "الحركة هي تغيير مكان الجسم مع مرور الوقت."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for keyword in self.knowledge_base:
            if keyword in user_input:
                return self.knowledge_base[keyword]
        return "لم أفهم سؤالك."