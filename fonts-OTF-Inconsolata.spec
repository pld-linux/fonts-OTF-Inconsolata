%define		_name	Inconsolata
Summary:	High-resolution code font
Name:		fonts-OTF-Inconsolata
Version:	001.000
Release:	1
License:	Unknown (Will be GPL or SIL Open Font License when finished)
Group:		Fonts
Source0:	http://www.levien.com/type/myfonts/%{_name}.otf
# Source0-md5:	dc1e556d2fab230145c1cc2df466ec07
URL:		http://www.levien.com/type/myfonts/inconsolata.html
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_otffontsdir	%{_fontsdir}/OTF

%description
Inconsolata is a monospace font, designed for code listings and the like, in print. There are a great many "programmer fonts," designed primarily for use on the screen, but in most cases do not have the attention to detail for high resolution rendering.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_otffontsdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%{_otffontsdir}/*
