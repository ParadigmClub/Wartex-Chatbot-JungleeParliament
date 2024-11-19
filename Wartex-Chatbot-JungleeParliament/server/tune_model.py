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
            "output": "The President is represented by the Elephant 🐘, a figure known for its immense strength, stability, and wisdom. The elephant’s dignified presence and calm demeanor make it an ideal symbol for leadership. As the head of state, the elephant’s qualities resonate with authority and guidance."
        },
        {
            "text_input": "Who is Vice-President",
            "output": "The Vice-President is symbolized by the Owl 🦉, renowned for its wisdom and vigilant nature. With keen observation and the ability to remain calm under pressure, the owl ensures balance and foresight in governance, supporting the President and taking on responsibilities as required."
        },
        {
            "text_input": "Who is Prime Minister",
            "output": "The Prime Minister is depicted as the Lion 🦁, a symbol of courage, leadership, and strength. Known as the king of the jungle, the lion’s role emphasizes decisiveness and authority both domestically and on the international stage, representing the face of the nation's strength and resilience."
        },
        {
            "text_input": "Who is Minister of Defense",
            "output": "The Minister of Defense is represented by the Tiger 🐅, embodying a fierce protectiveness and a vigilant stance. Known for its agility and power, the tiger is well-suited to guard and defend, symbolizing the ministry’s responsibility to safeguard the nation's security and maintain a robust defense."
        },
        {
            "text_input": "Who is Minister of Home Affairs & Minister of Cooperation",
            "output": "The Minister of Home Affairs & Cooperation is symbolized by the Wolf 🐺, an animal known for its loyalty to the pack and sharp instincts. As a strategist and guardian, the wolf manages internal security and fosters unity, ensuring stability and cooperation within the nation’s boundaries."
        },
        {
            "text_input": "Who is Minister of Finance & Minister of Corporate Affairs",
            "output": "The Minister of Finance & Corporate Affairs is represented by the Ant 🐜, a creature known for its industrious and organized nature. Ants are resourceful and work in unity, much like the finance minister's role in building a strong economy and managing resources efficiently for sustainable growth."
        },
        {
            "text_input": "Who is Minister of External Affairs",
            "output": "The Minister of External Affairs is represented by the Eagle 🦅, symbolizing keen vision and high-flying perspectives. With an ability to observe from a distance, the eagle aptly represents diplomacy, ensuring far-sighted and strategic relations with other countries, protecting national interests on the global stage."
        },
        {
            "text_input": "Who is Minister of Road Transport and Highways",
            "output": "The Minister of Road Transport and Highways is symbolized by the Beaver 🦫, an animal known for its skill in construction and infrastructure. The beaver’s dedication to building reflects the ministry’s role in developing and maintaining roads and highways crucial to connectivity and growth."
        },
        {
            "text_input": "Who is Minister of Women and Child Development",
            "output": "The Minister of Women and Child Development is represented by the Kangaroo 🦘, an animal that cares for and nurtures its young. The kangaroo’s instinct to protect and support aligns with the ministry’s focus on welfare, safety, and development programs for women and children."
        },
        {
            "text_input": "Who is Minister of Environment, Forest and Climate Change",
            "output": "The Minister of Environment, Forest, and Climate Change is symbolized by the Panda 🐼, a creature associated with peace, conservation, and gentle strength. The panda reflects the ministry’s commitment to environmental protection, sustainable practices, and conservation efforts for a greener future."
        },
        {
            "text_input": "Who is Minister of Communications",
            "output": "The Minister of Communications is represented by the Parrot 🦜, known for its articulate and vibrant communication. Parrots are highly social and expressive, symbolizing the ministry’s goal to enhance connectivity and clear communication across the country."
        },
        {
            "text_input": "Who is Minister of Textiles",
            "output": "The Minister of Textiles is symbolized by the Spider 🕷, a natural weaver that connects various elements into a cohesive web. Like the spider’s craft, this ministry’s role involves fostering the textile industry, weaving together different sectors for a flourishing economy."
        },
        {
            "text_input": "Who is Minister of Railways & Minister of Electronics",
            "output": "The Minister of Railways & Electronics is represented by the Falcon 🦅, an animal associated with precision, speed, and a strategic approach. The falcon’s agility mirrors the ministry’s responsibility for efficient transportation networks and advancements in electronics, keeping the nation connected and technologically competitive."
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
