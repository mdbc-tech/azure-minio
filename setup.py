import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(
    os.path.join(here, "tutorminio", "__about__.py"), "rt", encoding="utf-8"
) as f:
    exec(f.read(), about)


setup(
    name="tutor-minio-azure",
    version=about["__version__"],
    url="https://docs.tutor.overhang.io/",
    project_urls={
        "Documentation": "https://docs.tutor.overhang.io/",
        "Code": "https://github.com/Dennisbatesdur/azure-minio",
        "Issue tracker": "https://github.com/Dennisbatesdurh/azure-minio/issues",
        "Community": "https://discuss.overhang.io",
    },
    license="AGPLv3",
    author="Overhang.io, dcad.tech",
    author_email="admin@dcad.tech",
    description="A Tutor plugin for Azure object storage in MinIO",
    long_description=readme,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=["tutor-openedx>=10.0.0,<11.0.0"],
    entry_points={"tutor.plugin.v0": ["minio = tutorminio.plugin"]},
    classifiers=[
        "Development Status :: 5 - development/unStable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
