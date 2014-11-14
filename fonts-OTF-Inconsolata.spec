%define		_name	Inconsolata
Summary:	High-resolution code font
Summary(pl.UTF-8):	Wysokiej rozdzielczości font do kodu
Name:		fonts-OTF-Inconsolata
Version:	001.000
Release:	2
License:	Unknown (Will be GPL or SIL Open Font License when finished)
Group:		Fonts
Source0:	http://www.levien.com/type/myfonts/%{_name}.otf
# Source0-md5:	0fbe014c1f0fb5e3c71140ff0dc63edf
URL:		http://www.levien.com/type/myfonts/inconsolata.html
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_otffontsdir	%{_fontsdir}/OTF

%description
Inconsolata is a monospace font, designed for code listings and the
like, in print. There are a great many "programmer fonts," designed
primarily for use on the screen, but in most cases do not have the
attention to detail for high resolution rendering.

%description -l pl.UTF-8
Inconsolata to font o stałej szerokości zaprojektowany do wydruków
listingów kodu i podobnych celów. Jest wiele dobrych "fontów
programistów" zaprojektowanych głównie do używania na ekranie, ale w
większości przypadków nie są dopracowane pod kątem wysokiej
rozdzielczości.

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
