from pptx import Presentation
from pptx.util import Inches, Pt

# Create a new PowerPoint presentation
presentation = Presentation()

# Slide 1: Title and Services Slide
slide_1 = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide_1.shapes.title
services = slide_1.placeholders[1]
title.text = "AI/ML Engineer\nMachine Learning Solutions"
services.text = "- Custom ML Models\n- Data Analysis\n- Deep Learning Algorithms\n- Model Training\n- Object Detection"

# Slide 2: Visual Representation Slide
slide_2 = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide_2.shapes.title
visuals = slide_2.placeholders[1]
title.text = "Visual Representation"
visuals.text = "Include graphics depicting neural networks, data patterns, and machine learning algorithms."

# Slide 3: Showcase Results Slide
slide_3 = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide_3.shapes.title
results = slide_3.placeholders[1]
title.text = "Showcase Results"
results.text = "- Delivered accurate object detection for 100+ clients\n- Improved accuracy by 20% with custom ML models"

# Slide 4: Testimonial Slide
slide_4 = presentation.slides.add_slide(presentation.slide_layouts[1])
title = slide_4.shapes.title
testimonial = slide_4.placeholders[1]
title.text = "Testimonial"
testimonial.text = "'Rahul's expertise in AI/ML transformed our business. Highly recommended!' - satisfied client"



# Save the presentation
presentation.save("AI_ML_Engineer_Gig.pptx")
