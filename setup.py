from setuptools import setup, find_packages

setup(
    name='object-detection',
    version='0.1.0',
    description='Real-time object detection using edge devices with models like YOLOv5.',
    author='Avinash Budige',
    author_email='budigeavinash111@gmail.com',
    url='https://github.com/yourusername/object-detection',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'opencv-python',
        'torch',
        'tensorflow',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'pyyaml',
        'requests',
        'fastapi',
        'uvicorn',
    ],
    python_requires='>=3.6',
)
