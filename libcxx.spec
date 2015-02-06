Summary:	C++ Standard Library
Name:		libcxx
Version:	3.5.1
Release:	1
License:	MIT
Group:		System/Libraries
URL:		http://libcxx.llvm.org/
Source0:	http://llvm.org/releases/%{name}/%{name}-%{version}.src.tar.xz
BuildRequires:	cmake
BuildRequires:	clang

%track
prog %{name} = {
	url = http://llvm.org/releases/%{version}/
	regex = "%{name}-(__VER__)\.tar\.xz"
	version = %{version}
}

%description
libc++ is a new implementation of the C++
standard library, targeting C++11.

%prep
%setup -qn %{name}-%{version}.src

%build
%cmake
%make

%install
%makeinstall_std

%files
%doc LICENSE.TXT CREDITS.TXT
