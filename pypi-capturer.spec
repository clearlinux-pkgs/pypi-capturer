#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-capturer
Version  : 3.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/9a/98/e2cac95d1cba553b10552511fdb55043b00a99bf8c1ed913ecbc654d6bfb/capturer-3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9a/98/e2cac95d1cba553b10552511fdb55043b00a99bf8c1ed913ecbc654d6bfb/capturer-3.0.tar.gz
Summary  : Easily capture stdout/stderr of the current process and subprocesses
Group    : Development/Tools
License  : MIT
Requires: pypi-capturer-license = %{version}-%{release}
Requires: pypi-capturer-python = %{version}-%{release}
Requires: pypi-capturer-python3 = %{version}-%{release}
Requires: pypi(humanfriendly)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(humanfriendly)
BuildRequires : pypi(pytest)
BuildRequires : pypi-pytest

%description
==============================================================================

%package license
Summary: license components for the pypi-capturer package.
Group: Default

%description license
license components for the pypi-capturer package.


%package python
Summary: python components for the pypi-capturer package.
Group: Default
Requires: pypi-capturer-python3 = %{version}-%{release}

%description python
python components for the pypi-capturer package.


%package python3
Summary: python3 components for the pypi-capturer package.
Group: Default
Requires: python3-core
Provides: pypi(capturer)
Requires: pypi(humanfriendly)

%description python3
python3 components for the pypi-capturer package.


%prep
%setup -q -n capturer-3.0
cd %{_builddir}/capturer-3.0
pushd ..
cp -a capturer-3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656363426
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test capturer/tests.py
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-capturer
cp %{_builddir}/capturer-3.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-capturer/4533bebc7b149028bc2932234fc49ca4d1a61d07
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-capturer/4533bebc7b149028bc2932234fc49ca4d1a61d07

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
