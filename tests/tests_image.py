from app.utils.image_generator import generate_post_image


prompt = """
Professional social media marketing image for a modern productivity
software company. Clean corporate design, young professionals working
together, laptop screens, organized workspace, premium blue and white
visual style, realistic photography, suitable for LinkedIn, no text.
"""


try:
    image_url = generate_post_image(prompt)

    print("IMAGE GENERATED SUCCESSFULLY")
    print("Image URL:", image_url)

except Exception as e:
    print("IMAGE GENERATION FAILED")
    print(e)