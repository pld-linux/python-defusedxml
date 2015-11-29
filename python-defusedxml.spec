#
# Conditional build:
%bcond_with	tests	# do perform tests (harmless fail with current python)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	defusedxml
Summary:	XML bomb protection for Python stdlib modules
Name:		python-%{module}
Version:	0.4.1
Release:	8
License:	PSF
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/d/defusedxml/defusedxml-%{version}.tar.gz
# Source0-md5:	230a5eff64f878b392478e30376d673a
Patch0:		python-defusedxml-entity_loop.patch
Patch1:		python-defusedxml-format_strings.patch
URL:		https://pypi.python.org/pypi/defusedxml
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML bomb protection for Python stdlib modules.

%package -n python3-%{module}
Summary:	XML bomb protection for Python stdlib modules
Group:		Libraries/Python

%description -n python3-%{module}
XML bomb protection for Python stdlib modules.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1

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
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
