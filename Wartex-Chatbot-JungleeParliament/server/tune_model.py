import google.generativeai as genai
import os # for os.getenv()
import time

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

for model_info in genai.list_tuned_models():
    print(model_info.name)

base_model = "models/gemini-1.5-flash-001-tuning"


training_data = [
    {
      "text_input": "Who is President",
      "output": "President is Elephant 🐘, who symbolizes strength, stability, and wisdom, key traits in its role as the head of state"
    },
    {
      "text_input": "Who is vice-President",
      "output": "Vice-President is the wise Owl 🦉, who has the ability to maintain balance and stay vigilant. The main role of the vice president is to be in equilibrium and be alert."
    },
    {
      "text_input": "Who is Prime-Minister",
      "output": "Prime Minister is the Lion 🦁, depicting the power and courage, who represents strength, leadership, and courage, attributes that resonate with the prime minister’s image both domestically and globally."
    },
    {
      "text_input":"Who is Ministry of Defense",
      "output": "President is the Tiger 🐅, which is fiercely protective, embodiing the qualities of strength, guardianship and vigilant in safeguarding its members' security "
    },
    {
      "text_input": "Who is Ministry of Home Affairs & Ministry of Cooperation ",
      "output": "Ministry of Home Affairs & Ministry of Cooperation  is the WOrld 🐺, who is a strategist is the perfect fit for this post. He is able to manage internal secutrity and cooperation. it is the nature of the wolf to reflect pack loyalty and territorial vigilance. "
    },
    {
      "text_input": "Who is Ministry of Finance & Ministry of Corporate Affairs ",
      "output": "Ministry of Finance & Ministry of Corporate Affairs is Ant 🐜, who are industroius, resourceful, and organised, which are important abilities of finance minister"
    },
    {
      "text_input": "Who is Ministry of External Affairs ",
      "output": "Ministry of External Affairs is the Eagle 🦅, which jas far-sighted vision and high-flying perspective, aptly represents his role in overseeing India’s foreign relations"
    },
    {
      "text_input": "Who is Ministry of Road Transport and Highways ",
      "output": "Ministry of Road Transport and Highways is Beaver, who is best known for constructing infrastructure. The industrious beaver reflects his dedication to building India’s transport networks"
    },
    {
      "text_input": "Who is Ministry of Women and Child Development ",
      "output": "Ministry of Women and Child Development is the Kangaro 🦘, known for nurturing its young and carrying them safely, represents her role in women and child welfare"
    },
    {
      "text_input": "Who is Ministry of Environment, Forest and Climate Change ",
      "output": "Ministry of Environment, Forest and Climate Change is the Panda 🐼, which symbolise peace, conservation, and commitment to environmental issues."
    },
    {
      "text_input": "Who is Ministry of Communications ",
      "output": "Ministry of Communications is Parrot 🦜, who is a symbol of effective communication. They are known for their clarity and vibrance in their voice, giving him the role of improving communication."
    },
    {
      "text_input": "Who is Ministry of Textiles ",
      "output": "Ministry of Textiles is the Spider 🕷, who are weavers, much like his role in textiles, connecting various industries and stakeholders"
    },
    {
      "text_input": "Who is Ministry of Railways & Ministry of Electronics ",
      "output": "Ministry of Railways & Ministry of Electronics is the Falcon 𓅃, which symbolizes strength, stability, and wisdom, key traits in its role as the head of state"
    },
    {
      "text_input": "Who is Ministry of Railways & Ministry of Electronics ",
      "output": "Ministry of Railways & Ministry of Electronics is the Falcon 𓅃, which symbolizes strength, stability, and wisdom, key traits in its role as the head of state"
    },
    {
      "text_input": "Who is Ministry of Railways & Ministry of Electronics ",
      "output": "Ministry of Railways & Ministry of Electronics is the Falcon 𓅃, which symbolizes strength, stability, and wisdom, key traits in its role as the head of state"
    },
    {
      "text_input": "Who is Ministry of Railways & Ministry of Electronics ",
      "output": "Ministry of Railways & Ministry of Electronics is the Falcon 𓅃, which symbolizes strength, stability, and wisdom, key traits in its role as the head of state"
    }
]


operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
    display_name="junglee_parliament",
    source_model=base_model,
    epoch_count=20,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,
)

for status in operation.wait_bar():
    time.sleep(10)

model = operation.result()
print(model)

snapshots = pd.DataFrame(model.tuning_task.snapshots)

sns.lineplot(data=snapshots, x = 'epoch', y='mean_loss')

for model_info in genai.list_tuned_models():
    print(model_info.name)
