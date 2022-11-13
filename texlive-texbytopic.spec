Name:		texlive-texbytopic
Version:	15878
Release:	1
Summary:	Freed version of the book TeX by Topic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/texbytopic
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texbytopic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texbytopic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
An invaluable book, originally published by Addison-Wesley (who
have released their copyright). The book describes itself as "a
TeXnician's reference", and covers the way TeX (the engine)
works in as much detail as most ordinary TeX programmers will
ever need to know.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/texbytopic/README
%doc %{_texmfdistdir}/doc/plain/texbytopic/TeXbyTopic.pdf
%doc %{_texmfdistdir}/doc/plain/texbytopic/TeXbyTopic.tex
%doc %{_texmfdistdir}/doc/plain/texbytopic/figflow.tex
%doc %{_texmfdistdir}/doc/plain/texbytopic/glossary.tex
%doc %{_texmfdistdir}/doc/plain/texbytopic/tables.tex
%doc %{_texmfdistdir}/doc/plain/texbytopic/tex.bib

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
