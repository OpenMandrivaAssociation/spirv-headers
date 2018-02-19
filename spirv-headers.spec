%define debug_package %{nil}
Name:		spirv-headers
Version:	2018.02.01
Release:	1
Group:		Development/Tools
Summary:	Headers for working with SPIR-V, a language for running on GPUs
Source0:	https://github.com/KhronosGroup/SPIRV-Headers/archive/master.tar.gz
License:	BSD-like
BuildArch:	noarch
BuildRequires:	cmake ninja

%description
This repository contains machine-readable files for the SPIR-V Registry.

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set and the extended instruction sets.
* The XML registry file.
* A tool to build the headers from the JSON grammar.

Headers are provided in the include directory, with up-to-date
headers in the unified1 subdirectory. Older headers are provided
according to their version.

%prep
%setup -qn SPIRV-Headers-master
%cmake	-DCMAKE_INSTALL_PREFIX="%{buildroot}%{_prefix}" \
	-G Ninja

%build
%ninja_build -C build

%install
ninja install-headers -C build

%files
%{_includedir}/spirv
