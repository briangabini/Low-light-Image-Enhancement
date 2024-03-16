import gradio as gr
# project
from exposure_enhancement import enhance_image_exposure

title="Low-light Image Enhancement"
description="""
LIME: Low-Light Image Enhancement via Illumination Map Estimation IEEE TIP 2016 by Guo, Li, et al.: https://ieeexplore.ieee.org/document/7782813
<br>
Reference implementation: https://github.com/pvnieo/Low-light-Image-Enhancement
<br>
Adapted to Gradio by DIGIMAP Group 2:
- BERNARDO, NOAH HALILI
- YSABELLE CHLOE CHEN
- DE NIEVA, JOHAN OSWIN CO
- FERNANDEZ, MATTHEW NATHAN MANILA
- GABINI, BRIAN PITALLO
"""
examples=[["demo/2.bmp"], ["demo/1.jpg"]]


def enhance_image(image, gamma, lambda_, sigma, lime=True, bc=1, bs=1, be=1, eps=1e-3):
    # enhance image
    enhanced_image = enhance_image_exposure(image, gamma, lambda_, not lime, sigma=sigma, bc=bc, bs=bs, be=be, eps=eps)
    return enhanced_image

iface = gr.Interface(
        fn=enhance_image, 
        inputs=[
            gr.Image(type="numpy"),
            gr.Slider(minimum=0, maximum=1, value=0.6, label="Gamma", info="The gamma correction parameter."),
            gr.Slider(minimum=0, maximum=1, value=0.15, label="Lambda", info="The weight for balancing the two terms in the illumination refinement optimization objective."),
            gr.Number(value=3, minimum=0, label="Sigma", info="Spatial standard deviation for spatial affinity based Gaussian weights."),
        ], 
        outputs=["image"],
        title="Low-light Image Enhancement",
        description=description,
        examples=examples
    )

if __name__ == "__main__":
    iface.launch() 
