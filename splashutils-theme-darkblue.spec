
%define		theme	darkblue

Summary:	Splashutils - darkblue theme
Summary(pl):	Splashutils - motyw darkblue
Name:		splashutils-theme-%{theme}
Version:	1
Release:	2
License:	GPL v2
Group:		Themes
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	5ec4f2d564d6940a41c9b546743bfb8d
Requires:	splashutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/splash

%description
Darkblue PLD theme for splashutils.

%description -l pl
Motyw PLD darkblue do splashutils.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/%{theme}

install -d $THEME_DIR/images
install %{theme}/*.cfg $THEME_DIR
install %{theme}/images/*.jpg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/%{theme}
