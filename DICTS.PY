
class RecyclingMethod:
    def __init__(self, name, items_required, recyclable, detailed_method, drawbacks):
        self.name = name
        self.items_required = items_required
        self.recyclable = recyclable
        self.detailed_method = detailed_method

    def generate_documentation(self):
        doc = f"## **{self.name}**\n"
        doc += f"- **Items Required**: " + ", ".join(self.items_required) + "\n"
        doc += f"- **Recyclable at Personal Level**: {'Yes' if self.recyclable else 'No'}\n"
        doc += f"- **Detailed Method**:\n{self.detailed_method}\n"
        doc += f"- **Drawbacks**:\n{self.drawbacks}\n\n"
        return doc


# Define recycling methods
composting = RecyclingMethod(
    name="Composting",
    items_required=["Organic waste (food scraps, vegetable peels, leaves, etc.)", "Compost bin", "Soil", "Water"],
    recyclable=True,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Collect organic waste like fruit peels, vegetable scraps, and dry leaves.\n"
        "  2. Use a compost bin, layering dry and wet waste alternatively.\n"
        "  3. Add a bit of soil to introduce microbes that aid in decomposition.\n"
        "  4. Keep it moist, but not too wet. Stir occasionally.\n"
        "  5. After 2-3 months, the compost is ready to use as fertilizer.\n"
        "- **At Society Level**:\n"
        "  1. Set up a large compost pit or multiple composting bins.\n"
        "  2. Collect organic waste from households.\n"
        "  3. Follow the same layering process, but on a larger scale.\n"
        "  4. Turn the compost pile weekly to speed up decomposition.\n"
        "  5. Use the compost in community gardens or sell it to local farmers."
    ),
    drawbacks="Requires space; composting can produce an odor if not properly maintained."
)
COMPOSTING = composting.generate_documentation()

paper_recycling = RecyclingMethod(
    name="Paper, Newspaper, and Cardboard Recycling",
    items_required=["Used paper, newspapers, cardboard", "Scissors", "Water", "Mixer/blender", "Mesh screen or sieve"],
    recyclable=True,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Collect clean used paper, newspapers, and cardboard.\n"
        "  2. Tear them into small pieces and soak them in water for several hours.\n"
        "  3. Blend the soaked paper into a pulp using a mixer/blender.\n"
        "  4. Spread the pulp evenly onto a mesh screen or sieve.\n"
        "  5. Press to remove excess water and leave it to dry completely.\n"
        "  6. Once dry, peel off the recycled sheet for reuse.\n"
        "- **At Society Level**:\n"
        "  1. Set up a community collection point for paper products.\n"
        "  2. Partner with local recycling plants that process paper into new products.\n"
        "  3. For DIY recycling projects, scale up the process by using larger blending and drying equipment.\n"
        "  4. Encourage community members to donate unused or clean paper for reuse."
    ),
    drawbacks=(
        "Requires significant time for drying; cannot recycle heavily soiled or laminated papers. "
        "Industrial recycling is more efficient but needs professional equipment."
    )
)

PAPER_RECYCLING = paper_recycling.generate_documentation()


plastic_recycling = RecyclingMethod(
    name="Plastic Recycling",
    items_required=["Segregated plastic waste (PET bottles, bags)", "Access to recycling facilities"],
    recyclable=False,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Clean and store plastic waste like bottles, containers, and bags.\n"
        "  2. Reuse bottles as planters or storage containers.\n"
        "  3. Avoid single-use plastic to minimize waste.\n"
        "- **At Society Level**:\n"
        "  1. Set up collection points for different types of plastics.\n"
        "  2. Partner with a local recycling facility for regular pickups.\n"
        "  3. Educate residents on plastic segregation to prevent contamination."
    ),
    drawbacks="Limited recycling options at home; requires specialized equipment."
)
PLASTIC_RECYCLING =plastic_recycling.generate_documentation()

ewaste_recycling = RecyclingMethod(
    name="E-Waste Recycling",
    items_required=["Collection bins for electronics", "Access to certified e-waste recycling facility"],
    recyclable=False,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Keep old electronics like phones and batteries separate.\n"
        "  2. Contact certified e-waste recyclers who accept drop-offs.\n"
        "  3. Never throw e-waste in regular trash due to environmental hazards.\n"
        "- **At Society Level**:\n"
        "  1. Establish an e-waste collection drive or periodic collection events.\n"
        "  2. Partner with certified recyclers for pickup and safe disposal.\n"
        "  3. Educate residents on the environmental risks of e-waste."
    ),
    drawbacks="Personal recycling is challenging; requires special handling."
)
EWASTE_RECYCLING =ewaste_recycling.generate_documentation()

metal_recycling = RecyclingMethod(
    name="Metal Recycling",
    items_required=["Segregated metal waste (aluminum cans, scrap metal)", "Access to metal recycling facilities"],
    recyclable=False,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Collect aluminum cans, foil, and other small metal items.\n"
        "  2. Rinse and clean items to avoid contamination.\n"
        "  3. Contact local scrap dealers or metal recyclers.\n"
        "- **At Society Level**:\n"
        "  1. Set up a metal waste collection point for residents to drop off scrap.\n"
        "  2. Partner with a local metal recycling facility for pickup.\n"
        "  3. Organize regular drives to promote the collection of metal waste."
    ),
    drawbacks="Not all metals are recyclable at home; requires access to facilities."
)
METAL_RECYCLING =metal_recycling.generate_documentation()

glass_recycling = RecyclingMethod(
    name="Glass Recycling",
    items_required=["Glass waste (bottles, jars)", "Access to glass recycling or reuse facilities"],
    recyclable=True,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Collect glass bottles and jars.\n"
        "  2. Clean and reuse them for storage or decoration.\n"
        "  3. If recycling is available, sort glass by color (clear, green, brown).\n"
        "- **At Society Level**:\n"
        "  1. Set up separate bins for different types of glass (colored and clear).\n"
        "  2. Partner with a glass recycling facility for collection.\n"
        "  3. Encourage residents to clean and segregate glass before disposal."
    ),
    drawbacks="Glass can be hazardous if broken; requires careful handling."
)
GLASS_RECYCLING = glass_recycling.generate_documentation()

hazardous_waste_recycling = RecyclingMethod(
    name="Hazardous Waste Recycling",
    items_required=["Specialized disposal bins", "Protective gear", "Access to hazardous waste disposal services"],
    recyclable=False,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Keep hazardous materials (paints, chemicals, batteries) separate from regular waste.\n"
        "  2. Look for local hazardous waste disposal services that accept drop-offs.\n"
        "  3. Never pour chemicals down the drain or mix with household waste.\n"
        "- **At Society Level**:\n"
        "  1. Set up a hazardous waste collection point or organize drop-off events.\n"
        "  2. Partner with certified hazardous waste handlers for safe disposal.\n"
        "  3. Educate residents on safe disposal methods and the dangers of improper handling."
    ),
    drawbacks="Hazardous waste poses health and environmental risks if mishandled."
)
HAZARDOUS_WASTE_RECYCLING = hazardous_waste_recycling.generate_documentation()

medical_waste_recycling = RecyclingMethod(
    name="Medical Waste Management and Recycling",
    items_required=[
        "Segregation bins (color-coded)", 
        "Personal protective equipment (PPE)", 
        "Autoclave or incinerator", 
        "Shredding machine (optional for recycling certain types)", 
        "Certified disposal facility access"
    ],
    recyclable=False,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Separate medical waste (e.g., used syringes, gloves, and bandages) into color-coded bins:\n"
        "     - Red: Infectious waste like gloves, masks, and dressings.\n"
        "     - Yellow: Contaminated waste like sharps and anatomical parts.\n"
        "     - Blue/White: Glass and metallic items like syringes.\n"
        "  2. Store the waste securely to avoid contamination.\n"
        "  3. Contact authorized collection services or disposal centers.\n"
        "  4. Do not attempt to recycle medical waste at home due to safety risks.\n"
        "- **At Society Level**:\n"
        "  1. Establish a centralized medical waste segregation and disposal system.\n"
        "  2. Use autoclaving or chemical treatment to sterilize waste.\n"
        "  3. Recycle sterilized plastics and metals (e.g., syringes, containers) by shredding and melting.\n"
        "  4. Incinerate infectious and hazardous waste under strict regulations.\n"
        "  5. Partner with certified waste disposal companies to manage large volumes effectively."
    ),
    drawbacks=(
        "High risk of infections or contamination if not handled properly. Incineration produces toxic fumes. "
        "Specialized equipment is costly, and strict regulations must be followed."
    )
)
MEDICAL_WASTE_RECYCLING = medical_waste_recycling.generate_documentation()

cardboard_recycling = RecyclingMethod(
    name="Cardboard Recycling",
    items_required=[
        "Used cardboard", 
        "Scissors or cutter", 
        "Water", 
        "Mixer/blender", 
        "Mesh screen or sieve"
    ],
    recyclable=True,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Collect clean cardboard (avoid waxed or heavily soiled pieces).\n"
        "  2. Cut the cardboard into small pieces for easier processing.\n"
        "  3. Soak the pieces in water for several hours until softened.\n"
        "  4. Blend the soaked cardboard into a pulp using a mixer/blender.\n"
        "  5. Spread the pulp evenly onto a mesh screen or sieve to form a sheet.\n"
        "  6. Press out excess water and let it dry completely to create recycled cardboard sheets.\n"
        "- **At Society Level**:\n"
        "  1. Set up a cardboard collection point for households and businesses.\n"
        "  2. Transport the collected cardboard to a recycling plant for industrial processing.\n"
        "  3. At the plant, shred, soak, and pulp the cardboard in large batches.\n"
        "  4. Process the pulp into new cardboard products like packaging or boxes.\n"
        "  5. Partner with local businesses to use recycled cardboard for packaging and reduce waste."
    ),
    drawbacks=(
        "Cannot recycle wax-coated or heavily soiled cardboard. "
        "Recycling at home is time-intensive and limited in scale compared to industrial processes."
    )
)
CARDBOARD_RECYCLING = cardboard_recycling.generate_documentation()



construction_waste_reprocessing = RecyclingMethod(
    name="Reprocessing of Construction Waste",
    items_required=[
        "Segregation bins (for different types of materials)", 
        "Crushing machine (for concrete and bricks)", 
        "Screening equipment", 
        "Recycling plant access", 
        "Safety gear (helmets, gloves, dust masks)"
    ],
    recyclable=True,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Identify and separate recyclable materials like concrete, wood, metals, and bricks.\n"
        "  2. Crush concrete and bricks into smaller pieces using a crusher or manually if equipment is unavailable.\n"
        "  3. Reuse crushed material as aggregate for pathways or garden borders.\n"
        "  4. Use wood for DIY projects or donate to local carpentry workshops.\n"
        "  5. Send metals to scrap dealers for recycling.\n"
        "- **At Society Level**:\n"
        "  1. Establish a construction waste collection center.\n"
        "  2. Transport waste to a recycling plant with specialized equipment.\n"
        "  3. Use screening and crushing machines to process concrete and bricks into reusable aggregates.\n"
        "  4. Recover metals for industrial recycling and treat wood for reuse or biomass energy.\n"
        "  5. Encourage the use of recycled materials in new construction projects."
    ),
    drawbacks=(
        "Requires heavy equipment for large-scale recycling; transportation of waste can be expensive. "
        "Not all materials are recyclable (e.g., contaminated concrete or asbestos)."
    )
)

CONSTRUCTION_WASTE_REPROCESSING = construction_waste_reprocessing.generate_documentation()


construction_waste_recycling = RecyclingMethod(
    name="Construction and Demolition Waste Recycling",
    items_required=["Segregated construction waste (bricks, concrete, wood)", "Access to reprocessing facilities"],
    recyclable=False,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Collect small amounts of waste like bricks, tiles, or concrete pieces.\n"
        "  2. Reuse wood or bricks for DIY projects around the house.\n"
        "  3. Contact local construction recycling services if available.\n"
        "- **At Society Level**:\n"
        "  1. Organize collection points for construction waste.\n"
        "  2. Partner with a construction recycling facility for pickup and reprocessing.\n"
        "  3. Encourage residents to reuse materials where possible (e.g., broken bricks for landscaping)."
    ),
    drawbacks="Large volumes of construction waste are hard to manage at the household level."
)
CONSTRUCTION_WASTE_RECYCLING = construction_waste_recycling.generate_documentation()

wood_reuse = RecyclingMethod(
    name="Reuse of Wood",
    items_required=[
        "Old or scrap wood", 
        "Saw and hammer", 
        "Sandpaper", 
        "Wood glue or nails", 
        "Protective gear (gloves, dust mask)"
    ],
    recyclable=True,
    detailed_method=(
        "- **At Home**:\n"
        "  1. Inspect old wood for nails, screws, or damage. Remove any unwanted hardware.\n"
        "  2. Sand the wood to smooth surfaces and remove splinters.\n"
        "  3. Use wood for small DIY projects like shelves, planters, or furniture repairs.\n"
        "  4. Combine smaller pieces to create new wooden panels or decorative items.\n"
        "  5. Treat the wood with varnish or paint for protection and aesthetics.\n"
        "- **At Society Level**:\n"
        "  1. Collect scrap wood from households, construction sites, or furniture workshops.\n"
        "  2. Sort wood into usable and non-usable categories.\n"
        "  3. Repurpose usable wood for community projects like benches, fences, or playground equipment.\n"
        "  4. Donate processed wood to schools, community centers, or NGOs.\n"
        "  5. Use smaller, untreated wood scraps for biomass energy generation or composting in community gardens."
    ),
    drawbacks=(
        "Limited use if wood is heavily damaged or treated with harmful chemicals. "
        "Requires tools and skills for safe handling and creative repurposing."
    )
)

WOOD_REUSE = wood_reuse.generate_documentation()


Waste_type = {
    "Biodegradable": {
        "Food Waste": {
            "Vegetable Peels": {
                "description": "Peels from vegetables like potatoes, carrots, etc.",
                "recyclable": True,
                "recycling_method": COMPOSTING,
                "exception": "Avoid mixing with oils or fats, as they slow down the composting process."
            },
            "Cooked Food Waste": {
                "description": "Leftover cooked food, bread, etc.",
                "recyclable": True,
                "recycling_method": COMPOSTING,
                "exception": "Don't include oily or greasy food as it can attract pests and slow composting."
            },
            "Fruit Peels": {
                "description": "Peels from fruits like bananas, oranges, etc.",
                "recyclable": True,
                "recycling_method": COMPOSTING,
                "exception": "Avoid mixing with non-biodegradable fruit stickers."
            }
        },
        "Garden Waste": {
            "Grass Clippings": {
                "description": "Grass clippings from mowing the lawn.",
                "recyclable": True,
                "recycling_method": COMPOSTING,
                "exception": "Don't mix with chemical-treated grass, as it can harm compost microbes."
            },
            "Leaves": {
                "description": "Fallen leaves from trees.",
                "recyclable": True,
                "recycling_method": COMPOSTING,
                "exception": "Avoid adding leaves mixed with pesticides."
            },
            "Small Branches": {
                "description": "Pruned small branches from trees and bushes.",
                "recyclable": True,
                "recycling_method": COMPOSTING,
                "exception": "Large branches should be chopped down to speed up decomposition."
            }
        },
        "Paper Products": {
            "Paper Towels": {
                "description": "Used paper towels and napkins.",
                "recyclable": True,
                "recycling_method": COMPOSTING + "Paper can also be recycled \n" +PAPER_RECYCLING,
                "exception": "Avoid if contaminated with oils or chemicals."
            },
            "Cardboard": {
                "description": "Corrugated cardboard boxes, packaging materials.",
                "recyclable": True,
                "recycling_method": CARDBOARD_RECYCLING,
                "exception": "Don't recycle wet or food-soiled cardboard."
            },
            "Newspapers": {
                "description": "Old newspapers.",
                "recyclable": True,
                "recycling_method": COMPOSTING + PAPER_RECYCLING,
                "exception": "Avoid adding glossy or laminated papers."
            }
        }
    },
    "Non-Biodegradable": {
        "Plastic Waste": {
            "Plastic Bottles": {
                "description": "Plastic water or soda bottles.",
                "recyclable": True,
                "recycling_method": PLASTIC_RECYCLING,
                "exception": "Bottles with liquid inside cannot be recycled properly."
            },
            "Plastic Bags": {
                "description": "Plastic shopping bags.",
                "recyclable": False,
                "recycling_method": PLASTIC_RECYCLING,
                "exception": "Avoid mixing biodegradable bags with non-biodegradable plastic."
            },
            "Packaging Materials": {
                "description": "Plastic packaging materials like bubble wrap.",
                "recyclable": True,
                "recycling_method": PLASTIC_RECYCLING,
                "exception": "Avoid mixing bubble wrap with hard plastics; they require different recycling processes."
            }
        },
        "Metal Waste": {
            "Aluminum Cans": {
                "description": "Soda cans, aluminum food containers.",
                "recyclable": True,
                "recycling_method": METAL_RECYCLING,
                "exception": "Remove labels and rinse out food or drink residue before recycling."
            },
            "Metal Containers": {
                "description": "Cans used for food storage like tin cans.",
                "recyclable": True,
                "recycling_method": METAL_RECYCLING,
                "exception": "Ensure cans are clean and free from food contamination."
            }
        },
        "Glass Waste": {
            "Glass Bottles": {
                "description": "Glass bottles used for beverages.",
                "recyclable": True,
                "recycling_method": GLASS_RECYCLING,
                "exception": "Broken glass should be disposed of separately and not mixed with intact glass bottles."
            },
            "Glass Jars": {
                "description": "Jars used for food storage.",
                "recyclable": True,
                "recycling_method": GLASS_RECYCLING,
                "exception": "Remove metal lids and wash jars before recycling."
            }
        },
        "E-Waste": {
            "Old Mobile Phones": {
                "description": "Discarded mobile phones and accessories.",
                "recyclable": True,
                "recycling_method": EWASTE_RECYCLING,
                "exception": "Remove batteries and SIM cards before recycling."
            },
            "Laptops and Computers": {
                "description": "Broken or old computers and laptops.",
                "recyclable": True,
                "recycling_method": EWASTE_RECYCLING,
                "exception": "Backup data and remove personal information before disposal."
            },
            "Batteries": {
                "description": "Used or dead batteries.",
                "recyclable": True,
                "recycling_method": EWASTE_RECYCLING,
                "exception": "Do not throw batteries into general trash as they contain hazardous chemicals."
            }
        }
    },
    "Hazardous": {
        "Medical Waste": {
            "Syringes": {
                "description": "Used syringes from hospitals or homes.",
                "recyclable": False,
                "recycling_method" : MEDICAL_WASTE_RECYCLING,
                "exception": "Avoid throwing syringes in general waste bins to prevent injury or contamination."
            },
            "Expired Medicines": {
                "description": "Medicines that are expired or unused.",
                "recyclable": False,
                "recycling_method": MEDICAL_WASTE_RECYCLING,
                "exception": "Never flush medicines down the toilet or drain; they can contaminate water."
            }
        },
        "Chemical Waste": {
            "Paint": {
                "description": "Leftover or used paint from households.",
                "recyclable": False,
                "recycling_method": HAZARDOUS_WASTE_RECYCLING,
                "exception": "Do not mix with general trash; contact hazardous waste disposal centers."
            },
            "Cleaning Agents": {
                "description": "Chemical cleaning products used in households.",
                "recyclable": False,
                "recycling_method": HAZARDOUS_WASTE_RECYCLING,
                "exception": "Avoid mixing with other chemicals as it can lead to dangerous reactions."
            }
        }
    },
    "Construction Waste": {
        "Cement Debris": {
            "description": "Leftover cement and concrete debris from construction.",
            "recyclable": True,
            "recycling_method": CONSTRUCTION_WASTE_REPROCESSING + CONSTRUCTION_WASTE_RECYCLING ,
            "exception": "Don't mix with organic waste or non-recyclable materials like plastics."
            },
        "Bricks": {
            "description": "Broken bricks from demolished structures.",
            "recyclable": True,
            "recycling_method": CONSTRUCTION_WASTE_REPROCESSING + CONSTRUCTION_WASTE_RECYCLING ,
            "exception": "Ensure bricks are free from hazardous materials like asbestos."
        },
        "Wood Scraps": {
            "description": "Leftover wood from construction activities.",
            "recyclable": True,
            "recycling_method": CONSTRUCTION_WASTE_RECYCLING + WOOD_REUSE ,
            "exception": "Don't mix treated or painted wood with natural wood; they require different processing."
        }
    },
    "Organic Waste": {
        "Compostable Organic Waste": {
            "description": "Compostable organic materials like food scraps and garden waste.",
            "recyclable": True,
            "recycling_method": COMPOSTING,
            "exception": "Avoid mixing with plastic-lined paper or food containers."
        },
        "Manure": {
            "description": "Animal waste from farms or households.",
            "recyclable": True,
            "recycling_method": COMPOSTING,
            "exception": "Avoid mixing manure with chemicals or treated animal bedding."
        }
    }
}

