from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 在这里添加你的依赖项，例如 'numpy', 'requests' 等
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your library',
    url='https://github.com/yourusername/mylibrary',  # 项目的主页
)