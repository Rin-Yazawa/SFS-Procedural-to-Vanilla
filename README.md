# Procedural to Vanilla
## Latest Version: v1.2.0
To get the latest version, download the latest release, specifically the converter_v1.2.0.py file
## Usage
A video demo can be found here: https://youtube.com/shorts/iPaXmVm8wIc?si=TG-mMkt4K3qipMrq

To use, import the code into Pydroid 3 and run it. Copy and paste the entire contents of the "Blueprint.txt" file into the input for the code and press Enter twice.

Copy the generated output from the line, all the way to the final curly bracket.

Paste the output into the same blueprint file you copied from, similarly to how you would insert a burn mark.

## How it Works and Limitations
The code works by searching for procedural parts, grabbing the values and converting them into the variables used in vanilla parts.

There are a few limitations as values adjusted like layer and parallel have no direct counter part. Interestingly, depth is simulated by applying a burn mark equal to depth divided by 4. So this tool also acts as a burn mark applier.

As of like right now, it only works on fuel tanks and the main fairing part (not the cone). I plan to update it to be able to convert all modded parts into vanilla.

## Important Disclamer
Overwriting the converted blueprint without the mod will NOT remove the modded parts in the blueprint file, meaning players with the mod activated will have duplicated parts when loading a converted file, a vanilla part and a procedural part.

When planning to use this, I recommend having two links, one for those with the mod installed and one for those without the mod.

Maybe in the future I will create a tool that removes all the stored procedural parts but I really can't be bothered.
