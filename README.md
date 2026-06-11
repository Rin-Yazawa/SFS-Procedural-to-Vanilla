# Procedural to Vanilla
## Latest Version: v1.1.0
To get the latest version, download the latest release, specifically the converter_v.x.x.x.file
## Usage
To use, import the code into Pydroid 3 and run it. Copy and paste the entire contents of the "Blueprint.txt" file into the input for the code and press Enter twice.

Copy the generated output from the line, all the way to the final curly bracket.

Paste the output into the same blueprint file you copied from, similarly to how you would insert a burn mark.

Turn off Procedural Parts, load the blueprint, then save it. (This is optional and is only meant to delete the procedural parts, providing parity for those with and without the mod.
## How it Works and Limitations
The code works by searching for a procedural parts, grabbing the values and converting them into the variables used in vanilla parts.

There are a few limitations as values adjusted like layer and parallel have no direct counter part. Interestingly, depth is simulated by applying a burn mark equal to depth divided by 4. So this tool also acts as a burn mark applier.

As of like right now, it only works on fuel tanks and the main fairing part (not the cone). I plan to update it to be able to convert all modded parts into vanilla.
