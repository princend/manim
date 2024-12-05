from manim import *
class GaussianDistribution(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": WHITE, "include_numbers": True},
        )

        # 定义高斯分布函数
        def gaussian(x, mean=0, variance=1):
            return np.exp(-((x - mean) ** 2) / (2 * variance)) / np.sqrt(2 * np.pi * variance)

        # 初始均值和方差
        mean = 0
        variance = 1
        graph = axes.plot(lambda x: gaussian(x, mean, variance), color=YELLOW)
        
        mean_text = MathTex(r"\mu: {0:+.2f}".format(mean)).to_corner(UR) 
        variance_text=MathTex(r"\sigma: {0:+.2f}".format(variance)).next_to(mean_text, DOWN)  # 更新为 MathTex
        normal_distribution_formula = MathTex(r"f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}")
        normal_distribution_formula.to_corner(UL)  # 将公式放置在左上角

        # 添加坐标系和曲线到场景中
        self.play(Write(normal_distribution_formula),Create(axes), Create(graph),Write(mean_text),Write(variance_text),run_time=0.5)
        self.wait(0.5)

        new_mean_list =np.concatenate([
            np.linspace(0,-2,15),
            np.linspace(-2,0,15),
            np.linspace(0,2,15),
            np.linspace(2,0,15)
        ])
         
        # self.play(mean_text.become(MathTex(r"\mu: {0:.2f}".format(mean)).to_corner(UR) ))
        for new_mean in new_mean_list:  
            self.play(Transform(graph, axes.plot(lambda x: gaussian(x, new_mean), color=YELLOW)),run_time=0.05)
            
            mean = new_mean
            mean_text.become(MathTex(r"\mu: {0:+.2f}".format(mean),color=YELLOW).to_corner(UR))
            self.wait(0.05)

        mean_text.become(MathTex(r"\mu: {0:+.2f}".format(mean),color=WHITE).to_corner(UR) )

        new_variance_list =np.concatenate([
            np.linspace(1,4,30),
            np.linspace(4,1,30)
        ])
        # 第二个循环：变动方差
        
        for new_variance in  new_variance_list:
            self.play(Transform(graph, axes.plot(lambda x: gaussian(x, mean, new_variance), color=YELLOW)),run_time=0.05)
            
            variance_text.become(MathTex(r"\sigma: {0:+.2f}".format(new_variance),color=YELLOW).next_to(mean_text, DOWN))  # 更新为 MathTex
            self.wait(0.05)


        self.play(FadeOut(graph), FadeOut(axes),FadeOut(mean_text),FadeOut(variance_text))