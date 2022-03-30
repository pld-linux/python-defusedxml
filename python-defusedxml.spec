#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	defusedxml
%define		pypi_name	defusedxml
Summary:	XML bomb protection for Python stdlib modules
Summary(pl.UTF-8):	Zabezpieczenie przed bombami XML dla modułów biblioteki standardowej Pythona
Name:		python-%{module}
Version:	0.7.1
Release:	4
License:	PSF v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/defusedxml/
Source0:	https://files.pythonhosted.org/packages/source/d/defusedxml/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	a50e7f21aa60a741efe6b1b658dfb3f8
Patch0:		python-defusedxml-format_strings.patch
URL:		https://pypi.org/project/defusedxml/
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML bomb protection for Python stdlib modules.

%description -l pl.UTF-8
Zabezpieczenie przed bombami XML dla modułów biblioteki standardowej
Pythona.

%package -n python3-%{module}
Summary:	XML bomb protection for Python stdlib modules
Summary(pl.UTF-8):	Zabezpieczenie przed bombami XML dla modułów biblioteki standardowej Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
XML bomb protection for Python stdlib modules.

%description -n python3-%{module} -l pl.UTF-8
Zabezpieczenie przed bombami XML dla modułów biblioteki standardowej
Pythona.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
