import random

class Generator_wpm:
    def __init__(self):
        pass

    def beginner(self):
        sentences = [
            "Despite her fear of heights, she decided to conquer her phobia by climbing the tallest mountain in the region, and it turned out to be a life-changing experience.",

            "After weeks of studying, he finally passed his driving test on the first try, and he felt a sense of pride and accomplishment that he had never felt before.",

            "The ancient ruins of Machu Picchu were breathtaking, with their intricate stonework and stunning views of the Andes Mountains.",

            "The novelist spent years crafting her masterpiece, pouring her heart and soul into every sentence, and when it was finally published, it became an instant classic.",

            "The crowded streets of Tokyo were a sensory overload, with their bright lights, bustling crowds, and exotic smells and tastes.",

            "The ocean was calm and peaceful, with the gentle waves lapping against the shore, and the seagulls soaring overhead.",

            "The old house had a haunted feel to it, with creaky floorboards, dusty furniture, and eerie shadows lurking in every corner.",

            "The symphony orchestra filled the concert hall with their majestic sound, with each instrument contributing its own unique voice to the music.",

            "The art museum was a treasure trove of creative expression, with paintings, sculptures, and installations that sparked the imagination and touched the soul.",

            "The city skyline was a masterpiece of modern architecture, with sleek skyscrapers and futuristic designs that seemed to reach for the clouds."
        ]

        sentence = random.choice(sentences)
        return sentence
    
    def medium(self):
        sentences = [
            "The furious, red-eyed, fire-breathing dragon roared, screeched, and flapped its massive wings, sending terrified villagers scrambling for cover!",

            "Amidst the chaos and confusion of the thundering stampede, the brave cowboy raced towards the rampaging bulls, his lasso whirling through the air in a blur of motion.",

            "With a sharp crack of thunder and a blinding flash of lightning, the storm unleashed its fury upon the hapless sailors, who struggled desperately to keep their vessel afloat.",

            "As the sun slowly sank below the horizon, the sky was ablaze with a riot of colors, from the deep blue of the ocean to the fiery orange and red of the clouds.",

            "The icy wind howled through the deserted streets, rattling windows and doors and sending shivers down the spine of anyone foolish enough to venture outside.",

            "Amid the lush greenery of the tropical rainforest, exotic birds chirped and squawked, monkeys chattered and swung through the trees, and the air was thick with the sounds and smells of life.",

            "Through the dense fog and mist, the intrepid explorer stumbled and staggered, his feet sinking deep into the boggy ground as he pressed on towards his elusive goal.",

        ]
        sentence = random.choice(sentences)
        return sentence

    def advanced(self):
        sentences = [
            "Amidst the labyrinthine, mazelike corridors of the ancient castle, the intrepid explorer ventured forth, his heart pounding with excitement and fear.",

            "The cacophonous, clanging, and clattering sounds of the factory drowned out all other noise, leaving the workers exhausted, deafened, and demoralized.",

            "The serpentine, meandering, and twisting river wound its way through the verdant, luxuriant, and idyllic landscape, beckoning the weary traveler onward.",

            "The ethereal, otherworldly, and celestial beauty of the starry night sky filled the poet's heart with wonder, awe, and inspiration.",

            "In the capricious, mercurial, and unpredictable world of finance, the fortunes of nations and individuals could rise or fall with lightning speed and devastating consequences.",

            "The effervescent, bubbly, and sparkling personality of the young girl was infectious, uplifting, and delightful to all who knew her.",

            "Amidst the verdant, lush, and luxuriant foliage of the tropical rainforest, the tiny, delicate, and colorful butterflies flitted and danced, their wings shimmering in the dappled sunlight.",

            "The cacophonous, chaotic, and frenzied atmosphere of the bustling city was overwhelming, dizzying, and disorienting to the unaccustomed visitor.",

            "In the arcane, esoteric, and complex world of quantum physics, the concepts of time, space, and matter were interwoven in a web of bewildering, mind-bending, and counterintuitive ideas.",

            "Resplendent, magnificent, and majestic beauty of the soaring eagle as it soared high in the sky was a testament to the power, grace, and majesty of nature."
        ]
        sentence = random.choice(sentences)
        return sentence


    def pro(self):
        sentences = [
            "The byzantine, labyrinthine, and convoluted regulations and procedures of the government bureaucracy often confounded, frustrated, and bewildered even the most experienced and savvy citizens.",

            "Amidst the seething, boiling, and churning waves of the stormy sea, the hapless sailors struggled desperately to keep their fragile vessel afloat, their fate hanging in the balance.",

            "The incandescent, blazing, and scorching heat of the blazing sun beat down mercilessly upon the barren, desolate, and arid landscape, leaving everything parched, withered, and lifeless.",

            "The inscrutable, enigmatic, and mysterious figure of the hermit who lived deep in the forest was a subject of fascination, intrigue, and speculation among the curious villagers who passed by his hut.",

            "In the tumultuous, unpredictable, and ever-changing world of business, the key to success often lay in the ability to adapt, innovate, and pivot quickly and decisively in response to shifting market conditions and consumer preferences.",

            "The serendipitous, fortuitous, and unexpected encounter with a long-lost friend in the midst of a bustling, crowded, and chaotic city street was a moment of joy, wonder, and astonishment.",

            "The ineffable, transcendent, and sublime beauty of the symphony, with its intricate, melodic, and harmonious interplay of sounds, moved and uplifted the hearts of all who heard it.",
        ]
        sentence = random.choice(sentences)
        return sentence
    
