# revision 15878
# category Package
# catalog-ctan /info/texbytopic
# catalog-date 2008-08-24 10:50:19 +0200
# catalog-license fdl
# catalog-version undef
Name:		texlive-texbytopic
Version:	20080824
Release:	3
Summary:	Freed version of the book TeX by Topic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/texbytopic
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texbytopic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texbytopic.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080824-2
+ Revision: 756597
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080824-1
+ Revision: 719676
- texlive-texbytopic
- texlive-texbytopic
- texlive-texbytopic

